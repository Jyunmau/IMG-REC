from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap

import Qt_Ui.ui_singleResultWid as ui_singleResultWid
from Core import ImageRecognition


# _*_ coding:utf-8 _*_

#   @Version : 1.0.0
#   @Time    : 2020/01/01 14:52
#   @Author  : Jyunmau Chan
#   @File    : SingleResultWid.py


class SingleResultWid(QtWidgets.QWidget, ui_singleResultWid.Ui_SingleRec):
    """单张图片识别结果的窗体逻辑"""

    def __init__(self, img_rec: ImageRecognition):
        super(SingleResultWid, self).__init__()
        self.setupUi(self)
        # 设置图像处理实例
        self.img_rec = img_rec

    def image_predict(self, img):
        """调用图像处理实例进行识别，并将结果反馈到窗体上"""
        cate, acc = self.img_rec.image_predict(img)
        self.img_label.setPixmap(QPixmap.fromImage(img).scaled(self.img_label.height(), self.img_label.width()))
        self.result_label.setText(cate)
        self.acc_label.setText(acc)
