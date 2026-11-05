from PySide6.QtWidgets import QDialog

from res.dlg_about_app import Ui_DlgAboutApp


class DlgAboutApp(QDialog, Ui_DlgAboutApp):
    """ диалоговое окно О программе..."""
    def __init__(self, version: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.labelVerValue.setText(f"{version}")