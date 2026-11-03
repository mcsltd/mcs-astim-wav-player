import logging
from pathlib import Path

import sounddevice as sd
import soundfile as sf

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog

from res.main_window import Ui_MainWindow

logger = logging.getLogger(__name__)

def format_time(seconds):
    seconds = max(0, int(seconds))
    return f"{seconds // 60:02d}:{seconds % 60:02d}"

class WavPlayer:

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self._player = WavPlayer()
        self.pushButtonSelectWav.clicked.connect(self.on_selected_wav_clicked)
        self.pushButtonStart.clicked.connect(self.on_start_clicked)
        self.pushButtonStop.clicked.connect(self.on_stop_clicked)
        self.pushButtonPause.clicked.connect(self.on_pause_clicked)

        self._time_timer = QTimer(self)
        self._time_timer.setInterval(200)
        self._time_timer.timeout.connect(self.update_time_counter)

        self._set_output_devices()

    def _set_output_devices(self):
        hostapis = sd.query_hostapis()
        wasapi_indexes = [
            idx for idx, api in enumerate(hostapis)
            if "WASAPI" in api["name"]
        ]
        all_devices = sd.query_devices()
        for idx, device in enumerate(all_devices):
            if device["max_output_channels"] <= 0:
                continue
            if wasapi_indexes and device["hostapi"] not in wasapi_indexes:
                continue
            logger.debug(f"get device: {device}")
            self.comboBoxOutputDevices.addItem(device["name"], userData=device)

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
        self._player.load()
        self._time_timer.stop()
        self.update_time_counter()
        self.groupBox.setEnabled(True)
        self._enable_player()

    def update_time_counter(self):
        current = format_time(self._player.position)
        total = format_time(self._player.duration)
        self.labelTimeCounter.setText(f"[{current}/{total}]")

    def on_start_clicked(self):
        device = self.comboBoxOutputDevices.currentData()
        self._player.device = device["index"] if device else None
        self._player.start()
        self._time_timer.start()
        self.pushButtonPause.setText("Пауза")

    def on_pause_clicked(self):
        self._player.pause()
        if self._player.paused:
            self.pushButtonPause.setText("Продолжить")
        else:
            self.pushButtonPause.setText("Пауза")

    def on_stop_clicked(self):
        self._player.stop()
        self._time_timer.stop()
        self.update_time_counter()
        self.pushButtonPause.setText("Пауза")

    def _enable_player(self):
        self.pushButtonStart.setEnabled(True)
        self.pushButtonPause.setEnabled(True)
        self.pushButtonStop.setEnabled(True)

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