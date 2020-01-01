import cv2
import numpy as np
import keras
import glob

# _*_ coding:utf-8 _*_

#   @Version : 1.0.0
#   @Time    : 2020/01/01 15:26
#   @Author  : Jyunmau Chan
#   @File    : ImageRecognition.py

# ToDo 可选择加载不同模型

# 模型文件存放路径
model_path = "Models/cifar10_ResNet20v1_model.045.h5"


class ImageRecognition(object):
    """图片处理与识别"""

    def __init__(self):
        self.model = keras.models.load_model(model_path)
        # 模型可识别的类别（按序）
        self.category = ["airplane", "automobile", "bird", "cat",
                         "deer", "dog", "frog", "horse", "ship", "truck"]
        # 图片文件生成器
        self.image_it = None

    def image_predict(self, img):
        """
        用于单张图片识别
        :param img: QImage格式的图片
        :return: 预测分类，置信率
        """
        np_img = self._qimg2mat_format(img)
        y = self.model.predict(np.array([np_img]))
        _, cate_index = np.where(y == np.max(y, axis=1))
        return str(self.category[cate_index[0]]), str(np.max(y, axis=1))

    def set_images_path(self, dir_path):
        """
        生成文件夹内图片文件路径的生成器对象
        :param dir_path: 图片文件夹路径str
        :return:
        """
        images_path = glob.glob(dir_path + '/*' + 'jpg')
        self.image_it = self._get_image_path(images_path)

    def _get_image_path(self, images_path):
        """
        文件夹内图片文件路径的生成器
        :param images_path: 图片文件路径list
        :return:
        """
        for image_path in images_path:
            yield image_path

    def get_image_predict(self):
        """
        利用生成器获取图片并识别
        :return: 预测分类，置信率，图片文件路径
        """
        image_path = next(self.image_it)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (32, 32))
        image = image / 255.0
        y = self.model.predict(np.array([image]))
        _, cate_index = np.where(y == np.max(y, axis=1))
        return str(self.category[cate_index[0]]), str(np.max(y, axis=1)), image_path

    def _qimg2mat_format(self, img):
        """将QImage图片转换成cv的mat并格式化"""
        ptr = img.constBits()
        # QImage是四通道的RGBA8888（多一个alpha透明度通道）
        mat = np.array(ptr).reshape((img.height(), img.width(), 4))
        mat = cv2.cvtColor(mat, cv2.COLOR_RGBA2RGB)
        mat = cv2.resize(mat, (32, 32))
        mat = mat / 255.0
        return mat
