# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resultWid.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(521, 300)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.result_label = QLabel(Form)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.result_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.acc_label = QLabel(Form)
        self.acc_label.setObjectName(u"acc_label")
        self.acc_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.acc_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.img_label = QLabel(Form)
        self.img_label.setObjectName(u"img_label")
        self.img_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b\u7ed3\u679c\uff1a", None))
        self.result_label.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7f6e\u4fe1\u7387\uff1a", None))
        self.acc_label.setText("")
        self.img_label.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u5f20", None))
    # retranslateUi

