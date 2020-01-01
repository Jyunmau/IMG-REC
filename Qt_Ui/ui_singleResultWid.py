# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'singleResultWid.ui'
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

class Ui_SingleRec(object):
    def setupUi(self, SingleRec):
        if SingleRec.objectName():
            SingleRec.setObjectName(u"SingleRec")
        SingleRec.resize(604, 309)
        self.verticalLayout = QVBoxLayout(SingleRec)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(SingleRec)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.result_label = QLabel(SingleRec)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.result_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(SingleRec)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.acc_label = QLabel(SingleRec)
        self.acc_label.setObjectName(u"acc_label")
        self.acc_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.acc_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.img_label = QLabel(SingleRec)
        self.img_label.setObjectName(u"img_label")
        self.img_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img_label)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SingleRec)

        QMetaObject.connectSlotsByName(SingleRec)
    # setupUi

    def retranslateUi(self, SingleRec):
        SingleRec.setWindowTitle(QCoreApplication.translate("SingleRec", u"\u8bc6\u522b\u7ed3\u679c", None))
        self.label_2.setText(QCoreApplication.translate("SingleRec", u"\u8bc6\u522b\u7ed3\u679c\uff1a", None))
        self.result_label.setText("")
        self.label_4.setText(QCoreApplication.translate("SingleRec", u"\u7f6e\u4fe1\u7387\uff1a", None))
        self.acc_label.setText("")
        self.img_label.setText("")
    # retranslateUi

