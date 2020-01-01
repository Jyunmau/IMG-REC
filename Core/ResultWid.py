from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap

import Qt_Ui.ui_resultWid as ui_resultWid
from Core import ImageRecognition


# _*_ coding:utf-8 _*_

#   @Version : 1.0.0
#   @Time    : 2020/01/01 14:54
#   @Author  : Jyunmau Chan
#   @File    : ResultWid.py


class ResultWid(QtWidgets.QWidget, ui_resultWid.Ui_Form):
    """图片文件夹识别结果的窗体逻辑"""

    def __init__(self, img_rec: ImageRecognition):
        super(ResultWid, self).__init__()
        self.setupUi(self)
        # 设置图像处理实例
        self.img_rec = img_rec
        # 绑定按钮槽函数
        self.pushButton.clicked.connect(self.image_predict)

    def image_predict(self):
        """槽函数，展示预测结果，点击按钮可以处理下一张，末张之后关闭本窗体"""
        try:
            cate, acc, img_path = self.img_rec.get_image_predict()
            self.img_label.setPixmap(QPixmap(img_path).scaled(self.img_label.height(), self.img_label.width()))
            self.result_label.setText(cate)
            self.acc_label.setText(acc)
        except StopIteration:
            self.close()
