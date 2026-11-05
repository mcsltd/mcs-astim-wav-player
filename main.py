import logging
from pathlib import Path

import sounddevice as sd
import soundfile as sf

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QStyleFactory,
)

from config import DEBUG, DEVICE_NAME
from res.main_window import Ui_MainWindow
from res.waiting_dialog import WaitingDialog
from utils.device_monitor import (
    DeviceMonitor,
    find_astim_device,
    query_wasapi_output_devices,
    refresh_portaudio,
)

logger = logging.getLogger(__name__)

def format_time(seconds):
    seconds = max(0, int(seconds))
    return f"{seconds // 60:02d}:{seconds % 60:02d}"

class WavPlayer:
    """ Проигрыватель WAV-файла """
    def __init__(self):
        self._path_to_wav = None
        self.device = None
        self._data = None
        self._samplerate = None
        self._position = 0
        self._paused = False
        self._stream = None

    @property
    def path_to_wav(self):
        return self._path_to_wav
    @path_to_wav.setter
    def path_to_wav(self, path):
        self._path_to_wav = path

    @property
    def paused(self):
        return self._paused

    @property
    def active(self):
        return self._stream is not None and self._stream.active

    @property
    def opened(self):
        return self._stream is not None

    @property
    def duration(self):
        if self._data is None:
            return 0.0
        return len(self._data) / self._samplerate

    @property
    def position(self):
        if self._data is None:
            return 0.0
        return self._position / self._samplerate

    def load(self):
        self.stop()
        self._data, self._samplerate = sf.read(
            self._path_to_wav, dtype="float32", always_2d=True
        )
        self._position = 0
        logger.debug(f"loaded wav: {self._path_to_wav}, shape={self._data.shape}")

    def _callback(self, outdata, frames, time, status):
        if status:
            logger.warning(f"audio callback status: {status}")

        if self._paused:
            outdata.fill(0)
            return

        chunk = self._data[self._position:self._position + frames]
        outdata[:len(chunk)] = chunk

        if len(chunk) < frames:
            outdata[len(chunk):] = 0
            self._position = len(self._data)
            raise sd.CallbackStop

        self._position += frames

    def start(self):
        if self._data is None:
            logger.warning("wav file is not selected")
            return

        if self._stream is not None and self._stream.active:
            self._paused = False
            return

        if self._stream is not None:
            self._stream.close()
            self._stream = None

        if self._position >= len(self._data):
            self._position = 0

        self._paused = False
        extra = sd.WasapiSettings(exclusive=True)
        logger.debug(f"{self._samplerate=}")
        self._stream = sd.OutputStream(
            samplerate=self._samplerate,
            device=self.device,
            channels=self._data.shape[1],
            dtype="float32",
            callback=self._callback,
            extra_settings=extra
        )
        self._stream.start()

    def pause(self):
        if self._stream is not None and self._stream.active:
            self._paused = not self._paused

    def stop(self):
        if self._stream is not None:
            self._stream.stop()
            self._stream.close()
            self._stream = None
        self._position = 0
        self._paused = False

class MainWindow(QMainWindow, Ui_MainWindow):
    """ Главное окно проигрывателя VAW-файла. """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self._debug = False
        self._astim_connected = False
        self._wav_loaded = False
        self._pa_devices_dirty = False
        self._waiting_dialog = None

        self._player = WavPlayer()

        self.pushButtonSelectWav.clicked.connect(self.on_selected_wav_clicked)
        self.pushButtonStart.clicked.connect(self.on_start_clicked)
        self.pushButtonStop.clicked.connect(self.on_stop_clicked)
        self.pushButtonPause.clicked.connect(self.on_pause_clicked)
        self.actionExit.triggered.connect(self.close)


        self._time_timer = QTimer(self)
        self._time_timer.setInterval(200)
        self._time_timer.timeout.connect(self.update_time_counter)

        self.RecPlaybackBar.setStyle(QStyleFactory.create("Fusion"))

        self._device_monitor = DeviceMonitor(DEVICE_NAME, self)
        self._device_monitor.connection_changed.connect(
            self._on_astim_connection_changed
        )
        self._device_monitor.devices_changed.connect(
            self._on_audio_devices_changed
        )

        self.set_debug_mode(DEBUG)
        self.set_astim_connected(self._device_monitor.connected)
        self._set_output_devices()
        self._update_controls_state()

        QTimer.singleShot(0, self._check_startup_connection)

    def set_debug_mode(self, state: bool):
        """
        Переключение режима дебага.
        state = True - дебаг включен
        state = False - дебаг отключен
        """
        self._debug = state
        self.comboBoxOutputDevices.setVisible(state)
        self.labelDevicePlayer.setVisible(state)
        self._update_controls_state()

    def _check_startup_connection(self):
        self.set_astim_connected(self._device_monitor.connected)
        self._update_controls_state()

        if not self._debug and not self._device_monitor.connected:
            self._show_waiting_dialog(lost_connection=False)

    def _set_output_devices(self):
        current = self.comboBoxOutputDevices.currentData()
        current_name = current["name"] if current else None
        devices = query_wasapi_output_devices()
        astim_device = find_astim_device(devices, DEVICE_NAME)

        self.comboBoxOutputDevices.blockSignals(True)
        self.comboBoxOutputDevices.clear()
        for device in devices:
            logger.debug(f"get device: {device}")
            self.comboBoxOutputDevices.addItem(device["name"], userData=device)

        target = None
        if not self._debug:
            target = astim_device
        else:
            if current_name:
                target = next(
                    (device for device in devices if device["name"] == current_name),
                    None,
                )
            if target is None and devices:
                target = devices[0]

        if target is not None:
            self._select_output_device(target)
        else:
            self.comboBoxOutputDevices.setCurrentIndex(-1)

        self.comboBoxOutputDevices.blockSignals(False)

        selected = self.comboBoxOutputDevices.currentData()
        self._player.device = selected["index"] if selected else None

    def _select_output_device(self, target):
        for idx in range(self.comboBoxOutputDevices.count()):
            device = self.comboBoxOutputDevices.itemData(idx)
            if device and device["index"] == target["index"]:
                self.comboBoxOutputDevices.setCurrentIndex(idx)
                return

    def _reload_output_devices(self):
        if self._player.active:
            self._pa_devices_dirty = True
            return

        if self._player.opened:
            self._player.stop()

        refresh_portaudio()
        self._set_output_devices()
        self._pa_devices_dirty = False

    def _on_audio_devices_changed(self):
        self._pa_devices_dirty = True
        if not self._player.active:
            self._reload_output_devices()

    def _on_astim_connection_changed(self, connected: bool):
        self.set_astim_connected(connected)

        if not connected:
            if self._player.active:
                self.on_stop_clicked()
            if self._pa_devices_dirty:
                self._reload_output_devices()
            if not self._debug:
                self._show_waiting_dialog(lost_connection=True)
        else:
            if self._pa_devices_dirty and not self._player.active:
                self._reload_output_devices()
            self._close_waiting_dialog()

        self._update_controls_state()

    def _show_waiting_dialog(self, lost_connection: bool):
        if self._waiting_dialog is not None:
            self._waiting_dialog.set_lost_connection_mode(lost_connection)
            self._waiting_dialog.raise_()
            self._waiting_dialog.activateWindow()
            return

        dialog = WaitingDialog(
            DEVICE_NAME, self, lost_connection=lost_connection
        )
        dialog.rejected.connect(self._quit_application)
        dialog.finished.connect(self._on_waiting_dialog_finished)
        self._waiting_dialog = dialog
        dialog.open()

    def _on_waiting_dialog_finished(self, _result):
        self._waiting_dialog = None

    def _quit_application(self):
        app = QApplication.instance()
        if app is not None:
            app.quit()

    def _close_waiting_dialog(self):
        dialog = self._waiting_dialog
        if dialog is None:
            return

        self._waiting_dialog = None
        dialog.accept()

    def set_astim_connected(self, connected: bool):
        """Переключает цвет индикатора: True - зеленый, False - красный"""
        self._astim_connected = connected
        color = "#2ecc71" if connected else "#e74c3c"

        self.labelStatePlayer.setStyleSheet(
            f"""
            background-color: {color};
            border-radius: 8px;
            border: 1px solid #7f8c8d;
        """
        )
        state = "подключен" if connected else "не подключен"
        self.labelStatePlayer.setToolTip(f"{DEVICE_NAME} {state}")

    def _update_controls_state(self):
        can_play = self._wav_loaded and (
            self._debug or self._astim_connected
        )

        self.pushButtonStart.setEnabled(can_play and not self._player.active)
        self.pushButtonPause.setEnabled(can_play and self._player.active)
        self.pushButtonStop.setEnabled(self._player.active)

    def on_selected_wav_clicked(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите WAV файл для воспроизведения",
            "",
            "WAV файлы (*.wav);;Все файлы (*)",
            options=QFileDialog.Option.DontResolveSymlinks
        )
        if not path:
            return

        path_to_wav = Path(path)
        logger.debug(f"WAV file: {path_to_wav.name}")
        self.lineEditPathToWav.setText(path_to_wav.name)

        self._player.path_to_wav = str(path_to_wav)
        try:
            self._player.load()
        except Exception as exc:
            logger.exception("failed to load wav file")
            self._wav_loaded = False
            self._update_controls_state()
            QMessageBox.critical(
                self,
                "Ошибка",
                f"Не удалось открыть WAV-файл:\n{exc}",
            )
            return

        self._wav_loaded = True
        self._time_timer.stop()
        self.update_time_counter()
        self.groupBox.setEnabled(True)
        self._update_controls_state()

    def update_time_counter(self):
        duration = self._player.duration
        level = self._player.position / duration * 100 if duration else 0
        current = format_time(self._player.position)
        total = format_time(duration)

        self.RecPlaybackBar.setValue(level)
        self.labelTimeCounter.setText(f"[{current}/{total}]")

    def on_start_clicked(self):
        if not self._debug and not self._astim_connected:
            self._show_waiting_dialog(lost_connection=False)
            return

        if self._pa_devices_dirty and not self._player.active:
            self._reload_output_devices()

        device = self.comboBoxOutputDevices.currentData()
        if device is None:
            self._reload_output_devices()
            device = self.comboBoxOutputDevices.currentData()

        if device is None:
            QMessageBox.warning(
                self,
                "Устройство не найдено",
                f"Устройство {DEVICE_NAME} не найдено.",
            )
            return

        self._player.device = device["index"]
        try:
            self._player.start()
        except Exception as exc:
            logger.exception("failed to start playback")
            self._time_timer.stop()
            self._update_controls_state()
            QMessageBox.critical(
                self,
                "Ошибка воспроизведения",
                f"Не удалось запустить воспроизведение:\n{exc}",
            )
            return

        self._time_timer.start()
        self.pushButtonPause.setText("Пауза")
        self._update_controls_state()

    def on_pause_clicked(self):
        self._player.pause()
        if self._player.paused:
            self.pushButtonPause.setText("Продолжить")
        else:
            self.pushButtonPause.setText("Пауза")
        self._update_controls_state()

    def on_stop_clicked(self):
        self._player.stop()
        self._time_timer.stop()
        self.update_time_counter()
        self.pushButtonPause.setText("Пауза")
        self._update_controls_state()

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
        force=True
    )

def main():
    setup_logging()

    app = QApplication([])

    win = MainWindow()
    win.show()

    app.exec()


def create_vaw():
    from utils.create_wav import create_wav

    path = create_wav(
        output_dir="output",
        inter_stimulus_interval_ms=100,
        num_repetitions=100,
        syllable_wav="./vaw_files/DA+20.wav",
        add_inv=True,
        amplitude=1.0,
    )

if __name__ == "__main__":
    main()
    # create_vaw()
