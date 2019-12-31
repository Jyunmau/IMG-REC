import cv2
import numpy as np
import keras
import glob

model_path = "Models/cifar10_ResNet20v1_model.045.h5"


class ImageRecognition(object):
    def __init__(self):
        self.model = keras.models.load_model(model_path)
        self.category = ["airplane", "automobile", "bird", "cat",
                         "deer", "dog", "frog", "horse", "ship", "truck"]
        self.images_path = None
        self.image_it = None

    def image_predict(self, img):
        np_img = self._qimg2mat_format(img)
        y = self.model.predict(np.array([np_img]))
        _, cate_index = np.where(y == np.max(y, axis=1))
        print(self.category[cate_index[0]])

    def set_images_path(self, dir_path):
        self.images_path = glob.glob(dir_path + '/*' + 'jpg')
        self.image_it = self._get_image_path()

    def _get_image_path(self):
        for image_path in self.images_path:
            yield image_path

    def get_image_predict(self):
        image_path = next(self.image_it)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (32, 32))
        image = image / 255.0
        y = self.model.predict(np.array([image]))
        _, cate_index = np.where(y == np.max(y, axis=1))
        return str(self.category[cate_index[0]]), str(np.max(y, axis=1)), image_path

    def _qimg2mat_format(self, img):
        ptr = img.constBits()
        # 注意这地方通道数一定要填4，否则出错
        mat = np.array(ptr).reshape(img.height(), img.width(), 4)
        mat = cv2.cvtColor(mat, cv2.COLOR_RGBA2RGB)
        mat = cv2.resize(mat, (32, 32))
        mat = mat / 255.0
        # cv2.imshow('captureIMG', mat)
        # cv2.waitKey(0)
        return mat
