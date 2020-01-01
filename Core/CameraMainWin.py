from PySide2 import QtWidgets, QtMultimediaWidgets
from PySide2.QtGui import QImage
from PySide2.QtMultimedia import QCamera, QCameraViewfinderSettings, QCameraImageCapture
from PySide2.QtWidgets import QFileDialog

import Qt_Ui.ui_cameraWin as ui_cameraWin
from Core.ImageRecognition import ImageRecognition
from Core.ResultWid import ResultWid
from Core.SingleResultWid import SingleResultWid


# _*_ coding:utf-8 _*_

#   @Version : 1.0.0
#   @Time    : 2020/01/01 14:44
#   @Author  : Jyunmau Chan
#   @File    : CameraMainWin.py


class CameraMainWin(QtWidgets.QMainWindow, ui_cameraWin.Ui_MainWindow):
    """程序的主窗体逻辑"""

    def __init__(self, img_rec: ImageRecognition, res_wid: ResultWid, sig_res_wid: SingleResultWid):
        super(CameraMainWin, self).__init__()
        self.setupUi(self)
        # 设置图像处理实例和跳转实例
        self.img_rec = img_rec
        self.res_wid = res_wid
        self.sig_res_wid = sig_res_wid
        # camera设置
        self.camera = QCamera()
        self.camera.setCaptureMode(QCamera.CaptureViewfinder)
        self.cameraOpened = False  # 设置相机打开状态为未打开
        # 设置取景器分辨率
        view_finder_settings = QCameraViewfinderSettings()
        # viewFinderSettings.setResolution(800, 600)
        self.camera.setViewfinderSettings(view_finder_settings)
        # 初始化取景器
        self.viewCamera = QtMultimediaWidgets.QCameraViewfinder(self)
        self.camera.setViewfinder(self.viewCamera)
        self.cameraLayout.addWidget(self.viewCamera)  # 取景器放置到预留的布局中
        # 设置图像捕获
        self.capImg = QCameraImageCapture(self.camera)
        self.capImg.setCaptureDestination(QCameraImageCapture.CaptureToBuffer)
        self.capImg.imageCaptured.connect(self._process_captured_image)
        # 绑定按钮槽函数
        self.cameraButton.clicked.connect(self.switch_camera)
        self.captureButton.clicked.connect(self.take_pic)
        self.loadButton.clicked.connect(self.load_file)
        self.reconitionButton.clicked.connect(self.load_path)

    def switch_camera(self):
        """槽函数，开关摄像头"""
        if not self.cameraOpened:
            self.camera.start()
            self.cameraOpened = True
            self.cameraButton.setText("关闭摄像头")
        else:
            self.camera.stop()
            self.cameraOpened = False
            self.cameraButton.setText("打开摄像头")

    def take_pic(self):
        """槽函数，捕获摄像头图像"""
        self.capImg.capture()

    def _process_captured_image(self, _, img):
        """
        图像捕获时执行
        打开识别结果窗体并反馈预测结果
        :param img: 摄像头捕获到的QImage格式图片
        :return:
        """
        self.sig_res_wid.show()
        self.sig_res_wid.image_predict(img)

    def load_file(self):
        """槽函数，打开单个图片文件识别并弹窗反馈"""
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        qimage = QImage(fname)
        self.sig_res_wid.show()
        self.sig_res_wid.image_predict(qimage)

    def load_path(self):
        """槽函数，打开图片文件夹识别并弹窗反馈"""
        dir_path = QFileDialog.getExistingDirectory(self, '选择图片', 'c:\\')
        self.img_rec.set_images_path(dir_path)
        self.res_wid.show()
        self.res_wid.image_predict()
