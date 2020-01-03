# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameraWin.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chg_mod_Button = QPushButton(self.centralwidget)
        self.chg_mod_Button.setObjectName(u"chg_mod_Button")

        self.horizontalLayout.addWidget(self.chg_mod_Button)

        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")

        self.horizontalLayout.addWidget(self.loadButton)

        self.reconitionButton = QPushButton(self.centralwidget)
        self.reconitionButton.setObjectName(u"reconitionButton")

        self.horizontalLayout.addWidget(self.reconitionButton)

        self.captureButton = QPushButton(self.centralwidget)
        self.captureButton.setObjectName(u"captureButton")

        self.horizontalLayout.addWidget(self.captureButton)

        self.cameraButton = QPushButton(self.centralwidget)
        self.cameraButton.setObjectName(u"cameraButton")

        self.horizontalLayout.addWidget(self.cameraButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cameraLayout = QHBoxLayout()
        self.cameraLayout.setObjectName(u"cameraLayout")

        self.horizontalLayout_3.addLayout(self.cameraLayout)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u6df1\u5ea6\u795e\u7ecf\u7f51\u7edc\u7684\u56fe\u7247\u8bc6\u522b\u7a0b\u5e8f", None))
        self.chg_mod_Button.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u6a21\u578b", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u672c\u5730\u56fe\u7247", None))
        self.reconitionButton.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u672c\u5730\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.captureButton.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u7167", None))
        self.cameraButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.groupBox.setTitle("")
    # retranslateUi

