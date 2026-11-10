from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from res.dlg_about_app import Ui_DlgAboutApp


class DlgAboutApp(QDialog, Ui_DlgAboutApp):
    """ диалоговое окно О программе..."""
    def __init__(self, version: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.labelVerValue.setText(f"{version}")

        self.labelMcsSite.setText("<a href='https://mks.ru/ru'>https://mks.ru/ru</a>")
        self.labelMcsSite.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.labelMcsSite.setOpenExternalLinks(True)