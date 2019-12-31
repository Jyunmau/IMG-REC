import sys

import cv2
import numpy as np
from PySide2 import QtWidgets, QtMultimediaWidgets
from PySide2.QtGui import QPixmap, QImage
from PySide2.QtMultimedia import QCamera, QCameraViewfinderSettings, QCameraImageCapture
from PySide2.QtWidgets import QFileDialog

import Qt_Ui.ui_cameraWin as ui_cameraWin
from Core.ResultWid import ResultWid
from Core.ImageRecognition import ImageRecognition


class CameraMainWin(QtWidgets.QMainWindow, ui_cameraWin.Ui_MainWindow):
    def __init__(self, img_rec: ImageRecognition):
        super(CameraMainWin, self).__init__()
        self.setupUi(self)
        # 设置图像处理实例
        self.img_rec = img_rec
        # camera设置
        self.camera = QCamera()
        self.camera.setCaptureMode(QCamera.CaptureViewfinder)
        self.cameraOpened = False  # 设置相机打开状态为未打开
        # 设置取景器分辨率
        viewFinderSettings = QCameraViewfinderSettings()
        # viewFinderSettings.setResolution(800, 600)
        self.camera.setViewfinderSettings(viewFinderSettings)
        # 初始化取景器
        self.viewCamera = QtMultimediaWidgets.QCameraViewfinder(self)
        self.camera.setViewfinder(self.viewCamera)
        self.cameraLayout.addWidget(self.viewCamera)  # 取景器放置到预留的布局中
        # 设置图像捕获
        self.capImg = QCameraImageCapture(self.camera)
        self.capImg.setCaptureDestination(QCameraImageCapture.CaptureToBuffer)
        self.capImg.imageCaptured.connect(self._process_captured_image)
        # 绑定按钮函数
        self.cameraButton.clicked.connect(self.switch_camera)
        self.captureButton.clicked.connect(self.take_pic)
        self.loadButton.clicked.connect(self.load_file)

    def switch_camera(self):
        if not self.cameraOpened:
            self.camera.start()  # 打开相机
            self.cameraOpened = True
            self.cameraButton.setText("关闭摄像头")
        else:
            self.camera.stop()  # 关闭相机
            self.cameraOpened = False
            self.cameraButton.setText("打开摄像头")

    def take_pic(self):  # 拍照响应槽函数，照片保存到文件
        self.capImg.capture()

    def _process_captured_image(self, requestId, img):
        """捕捉到的图像转换成cv::mat"""
        self.img_rec.image_predict(img)

    def load_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        # self.label.setPixmap(QPixmap(fname))
        qimage = QImage(fname)
        self.img_rec.image_predict(qimage)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    W = CameraMainWin()
    Y = ResultWid()
    W.reconitionButton.clicked.connect(Y.show)
    W.show()
    sys.exit(app.exec_())
