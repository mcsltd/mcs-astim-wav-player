from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
)


class WaitingDialog(QDialog):
    def __init__(self, device_name: str, parent=None, lost_connection: bool = False):
        super().__init__(parent)
        self._device_name = device_name
        self._lost_connection = lost_connection

        self.setWindowTitle(self.tr("Ожидание A-Stim"))
        self.setModal(True)
        self.setMinimumWidth(420)
        self.setWindowFlag(Qt.WindowType.WindowContextHelpButtonHint, False)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        self.labelTitle = QLabel(self)
        font = self.labelTitle.font()
        font.setPointSize(12)
        font.setBold(True)
        self.labelTitle.setFont(font)
        layout.addWidget(self.labelTitle)

        self.labelMessage = QLabel(self)
        font = self.labelMessage.font()
        font.setPointSize(10)
        self.labelMessage.setFont(font)
        self.labelMessage.setWordWrap(True)
        layout.addWidget(self.labelMessage)

        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0, 0)
        self.progressBar.setTextVisible(False)
        layout.addWidget(self.progressBar)

        buttons = QHBoxLayout()
        buttons.addStretch()
        self.pushButtonExit = QPushButton(self.tr("Выход"), self)
        self.pushButtonExit.clicked.connect(self._on_exit_clicked)
        buttons.addWidget(self.pushButtonExit)
        layout.addLayout(buttons)

        self.set_lost_connection_mode(lost_connection)

    def set_lost_connection_mode(self, lost_connection: bool):
        self._lost_connection = lost_connection
        if lost_connection:
            self.labelTitle.setText(self.tr("Соединение потеряно"))
            message = self.tr(
                "%1 было отключено.\n\nПодключите его снова..."
            ).replace("%1", self._device_name)
        else:
            self.labelTitle.setText(self.tr("Ожидание подключения"))
            message = self.tr(
                "%1 не найдено.\n\nПодключите его к компьютеру..."
            ).replace("%1", self._device_name)
        self.labelMessage.setText(message)

    def retranslate(self):
        """ обновление текстов диалога после смены языка """
        self.setWindowTitle(self.tr("Ожидание A-Stim"))
        self.pushButtonExit.setText(self.tr("Выход"))
        self.set_lost_connection_mode(self._lost_connection)

    def _on_exit_clicked(self):
        self.reject()

    def showEvent(self, event):
        super().showEvent(event)
        self.raise_()
        self.activateWindow()
