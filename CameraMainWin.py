import sys

import cv2
import numpy as np
from PySide2 import QtWidgets, QtMultimediaWidgets
from PySide2.QtGui import QPixmap, QImage
from PySide2.QtMultimedia import QCamera, QCameraViewfinderSettings, QCameraImageCapture
from PySide2.QtWidgets import QFileDialog

import ui_cameraWin


class CameraMainWin(QtWidgets.QMainWindow, ui_cameraWin.Ui_MainWindow):
    def __init__(self):
        super(CameraMainWin, self).__init__()
        self.setupUi(self)
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
        self.capImg.imageCaptured.connect(self.process_captured_image)
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

    def process_captured_image(self, requestId, img):
        """捕捉到的图像转换成cv::mat"""
        ptr = img.constBits()
        mat = np.array(ptr).reshape(img.height(), img.width(), 4)  # 注意这地方通道数一定要填4，否则出错
        cv2.imshow('captureIMG', mat)
        cv2.waitKey(0)
        # todo 这里用观察者模式把图片传给图片处理实例

    def load_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        # self.label.setPixmap(QPixmap(fname))
        qimage = QImage(fname)
        ptr = qimage.constBits()
        mat = np.array(ptr).reshape(qimage.height(), qimage.width(), 4)  # 注意这地方通道数一定要填4，否则出错
        cv2.imshow('captureIMG', mat)
        cv2.waitKey(0)
        # todo 这里用观察者模式把图片传给图片处理实例


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    W = CameraMainWin()
    W.show()
    sys.exit(app.exec_())
