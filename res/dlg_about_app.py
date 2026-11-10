# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_about_appEjbdrm.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import res.resources_rc

class Ui_DlgAboutApp(object):
    def setupUi(self, DlgAboutApp):
        if not DlgAboutApp.objectName():
            DlgAboutApp.setObjectName(u"DlgAboutApp")
        DlgAboutApp.resize(511, 361)
        self.horizontalLayout_2 = QHBoxLayout(DlgAboutApp)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label = QLabel(DlgAboutApp)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(150, 150))
        self.label.setMaximumSize(QSize(150, 150))
        self.label.setPixmap(QPixmap(u":/images/icon.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.labelAppName = QLabel(DlgAboutApp)
        self.labelAppName.setObjectName(u"labelAppName")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.labelAppName.setFont(font)

        self.verticalLayout.addWidget(self.labelAppName)

        self.label_2 = QLabel(DlgAboutApp)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelVer = QLabel(DlgAboutApp)
        self.labelVer.setObjectName(u"labelVer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelVer.sizePolicy().hasHeightForWidth())
        self.labelVer.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.labelVer)

        self.labelVerValue = QLabel(DlgAboutApp)
        self.labelVerValue.setObjectName(u"labelVerValue")

        self.horizontalLayout_3.addWidget(self.labelVerValue)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(DlgAboutApp)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.labelMcsSite = QLabel(DlgAboutApp)
        self.labelMcsSite.setObjectName(u"labelMcsSite")
        self.labelMcsSite.setStyleSheet(u"https://mks.ru/ru")

        self.verticalLayout.addWidget(self.labelMcsSite)

        self.label_4 = QLabel(DlgAboutApp)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgAboutApp)

        QMetaObject.connectSlotsByName(DlgAboutApp)
    # setupUi

    def retranslateUi(self, DlgAboutApp):
        DlgAboutApp.setWindowTitle(QCoreApplication.translate("DlgAboutApp", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435...", None))
        self.label.setText("")
        self.labelAppName.setText(QCoreApplication.translate("DlgAboutApp", u"AstimWavPlayer", None))
        self.label_2.setText(QCoreApplication.translate("DlgAboutApp", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0430 \u0434\u043b\u044f\n"
"\u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044f WAV-\u0444\u0430\u0439\u043b\u043e\u0432 \u043d\u0430\n"
"MCS A-stim R1.1", None))
        self.labelVer.setText(QCoreApplication.translate("DlgAboutApp", u"\u0412\u0435\u0440\u0441\u0438\u044f:", None))
        self.labelVerValue.setText(QCoreApplication.translate("DlgAboutApp", u"v0.1.0", None))
        self.label_3.setText(QCoreApplication.translate("DlgAboutApp", u"\u00a9 2026 \u041e\u041e\u041e \"\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u0438\u0435 \u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u044b\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b\"", None))
        self.labelMcsSite.setText(QCoreApplication.translate("DlgAboutApp", u"...", None))
        self.label_4.setText(QCoreApplication.translate("DlgAboutApp", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u044f: MIT License", None))
    # retranslateUi

