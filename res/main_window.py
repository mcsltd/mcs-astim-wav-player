# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowWVoeJe.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)
import res.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(661, 309)
        icon = QIcon()
        icon.addFile(u":/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionRus = QAction(MainWindow)
        self.actionRus.setObjectName(u"actionRus")
        self.actionEng = QAction(MainWindow)
        self.actionEng.setObjectName(u"actionEng")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.labelDevicePlayer = QLabel(self.centralwidget)
        self.labelDevicePlayer.setObjectName(u"labelDevicePlayer")
        font = QFont()
        font.setPointSize(11)
        self.labelDevicePlayer.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelDevicePlayer)

        self.comboBoxOutputDevices = QComboBox(self.centralwidget)
        self.comboBoxOutputDevices.setObjectName(u"comboBoxOutputDevices")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBoxOutputDevices)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditPathToWav = QLineEdit(self.centralwidget)
        self.lineEditPathToWav.setObjectName(u"lineEditPathToWav")
        self.lineEditPathToWav.setEnabled(False)

        self.horizontalLayout.addWidget(self.lineEditPathToWav)

        self.pushButtonSelectWav = QPushButton(self.centralwidget)
        self.pushButtonSelectWav.setObjectName(u"pushButtonSelectWav")
        self.pushButtonSelectWav.setFont(font)

        self.horizontalLayout.addWidget(self.pushButtonSelectWav)


        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.labelPlayer = QLabel(self.centralwidget)
        self.labelPlayer.setObjectName(u"labelPlayer")
        self.labelPlayer.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.labelPlayer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.labelStatePlayer = QLabel(self.centralwidget)
        self.labelStatePlayer.setObjectName(u"labelStatePlayer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStatePlayer.sizePolicy().hasHeightForWidth())
        self.labelStatePlayer.setSizePolicy(sizePolicy)
        self.labelStatePlayer.setMinimumSize(QSize(16, 16))
        self.labelStatePlayer.setMaximumSize(QSize(16, 16))
        self.labelStatePlayer.setStyleSheet(u"background-color: #e74c3c;\n"
"            border-radius: 8px;\n"
"            border: 1px solid #7f8c8d;")
        self.labelStatePlayer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelStatePlayer)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.LabelRole, self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.formLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonStart = QPushButton(self.groupBox)
        self.pushButtonStart.setObjectName(u"pushButtonStart")
        self.pushButtonStart.setEnabled(False)
        self.pushButtonStart.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/images/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonStart.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButtonStart)

        self.pushButtonStop = QPushButton(self.groupBox)
        self.pushButtonStop.setObjectName(u"pushButtonStop")
        self.pushButtonStop.setEnabled(False)
        self.pushButtonStop.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/images/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonStop.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButtonStop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.RecPlaybackBar = QProgressBar(self.groupBox)
        self.RecPlaybackBar.setObjectName(u"RecPlaybackBar")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setKerning(True)
        self.RecPlaybackBar.setFont(font1)
        self.RecPlaybackBar.setAutoFillBackground(False)
        self.RecPlaybackBar.setStyleSheet(u"QProgressBar {\n"
"        text-align: center;\n"
"        padding: 0px;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #2ecc71;\n"
"        margin: 0px;\n"
"    }")
        self.RecPlaybackBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.RecPlaybackBar)

        self.labelTimeCounter = QLabel(self.groupBox)
        self.labelTimeCounter.setObjectName(u"labelTimeCounter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelTimeCounter.sizePolicy().hasHeightForWidth())
        self.labelTimeCounter.setSizePolicy(sizePolicy1)
        self.labelTimeCounter.setMaximumSize(QSize(150, 16777215))
        self.labelTimeCounter.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelTimeCounter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonVolumeReset = QPushButton(self.centralwidget)
        self.pushButtonVolumeReset.setObjectName(u"pushButtonVolumeReset")
        sizePolicy.setHeightForWidth(self.pushButtonVolumeReset.sizePolicy().hasHeightForWidth())
        self.pushButtonVolumeReset.setSizePolicy(sizePolicy)
        self.pushButtonVolumeReset.setMaximumSize(QSize(30, 30))
        self.pushButtonVolumeReset.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/volume.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonVolumeReset.setIcon(icon3)
        self.pushButtonVolumeReset.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.pushButtonVolumeReset)

        self.horizontalSliderVolume = QSlider(self.centralwidget)
        self.horizontalSliderVolume.setObjectName(u"horizontalSliderVolume")
        sizePolicy.setHeightForWidth(self.horizontalSliderVolume.sizePolicy().hasHeightForWidth())
        self.horizontalSliderVolume.setSizePolicy(sizePolicy)
        self.horizontalSliderVolume.setMinimumSize(QSize(150, 0))
        self.horizontalSliderVolume.setMaximumSize(QSize(200, 16777215))
        self.horizontalSliderVolume.setValue(50)
        self.horizontalSliderVolume.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSliderVolume.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.horizontalLayout_6.addWidget(self.horizontalSliderVolume)

        self.labelVolumeValue = QLabel(self.centralwidget)
        self.labelVolumeValue.setObjectName(u"labelVolumeValue")
        sizePolicy1.setHeightForWidth(self.labelVolumeValue.sizePolicy().hasHeightForWidth())
        self.labelVolumeValue.setSizePolicy(sizePolicy1)
        self.labelVolumeValue.setMinimumSize(QSize(30, 0))
        self.labelVolumeValue.setMaximumSize(QSize(30, 16777215))
        self.labelVolumeValue.setFont(font)

        self.horizontalLayout_6.addWidget(self.labelVolumeValue)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 661, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuLang = QMenu(self.menu)
        self.menuLang.setObjectName(u"menuLang")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menu.addAction(self.menuLang.menuAction())
        self.menu.addAction(self.actionAbout)
        self.menuLang.addAction(self.actionRus)
        self.menuLang.addAction(self.actionEng)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AstimWavPlayer", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435...", None))
        self.actionRus.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.actionEng.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.labelDevicePlayer.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0433\u0440\u044b\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"WAV-\u0444\u0430\u0439\u043b", None))
        self.pushButtonSelectWav.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c...", None))
        self.labelPlayer.setText(QCoreApplication.translate("MainWindow", u"MCS A-stim R.1.1", None))
        self.labelStatePlayer.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435", None))
        self.pushButtonStart.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.pushButtonStop.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.RecPlaybackBar.setFormat("")
        self.labelTimeCounter.setText(QCoreApplication.translate("MainWindow", u"00:00 / 00:00", None))
#if QT_CONFIG(tooltip)
        self.pushButtonVolumeReset.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c 50%", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonVolumeReset.setText("")
        self.labelVolumeValue.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.menuLang.setTitle(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a", None))
    # retranslateUi

