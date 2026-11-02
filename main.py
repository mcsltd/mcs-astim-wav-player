import logging
from pathlib import Path

import sounddevice as sd

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog

from res.main_window import Ui_MainWindow

logger = logging.getLogger(__name__)

class WavPlayer:

    def __init__(self):
        self._path_to_wav = None

    @property
    def path_to_wav(self):
        return self._path_to_wav
    @path_to_wav.setter
    def path_to_wav(self, path):
        self._path_to_wav = path

    def start(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self._player = WavPlayer()
        self.pushButtonSelectWav.clicked.connect(self.on_selected_wav_clicked)
        self.pushButtonStart.clicked.connect(self._player.start)
        self.pushButtonStop.clicked.connect(self._player.stop)
        self.pushButtonPause.clicked.connect(self._player.pause)

        self._set_output_devices()

    def _set_output_devices(self):
        all_devices = sd.query_devices()
        for idx, device in enumerate(all_devices):
            if device["max_output_channels"] > 0:
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
        path_to_wav = Path(path)
        logger.debug(f"WAV file: {path_to_wav.name}")
        self.lineEditPathToWav.setText(path_to_wav.name)

    def _enable_player(self):
        self.pushButtonStart.setEnabled(True)

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
        force=True
    )

if __name__ == "__main__":
    setup_logging()

    app = QApplication([])

    win = MainWindow()
    win.showMaximized()

    app.exec()