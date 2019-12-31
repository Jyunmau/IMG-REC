from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap

import Qt_Ui.ui_resultWid as ui_resultWid
from Core import ImageRecognition


class ResultWid(QtWidgets.QWidget, ui_resultWid.Ui_Form):
    def __init__(self, img_rec: ImageRecognition):
        super(ResultWid, self).__init__()
        self.setupUi(self)
        self.img_rec = img_rec
        self.pushButton.clicked.connect(self.image_predict)

    def image_predict(self):
        cate, acc, img_path = self.img_rec.get_image_predict()
        self.img_label.setPixmap(QPixmap(img_path).scaled(self.img_label.height(), self.img_label.width()))
        self.result_label.setText(cate)
        self.acc_label.setText(acc)
