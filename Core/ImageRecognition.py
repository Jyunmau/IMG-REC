import cv2
import numpy as np
import keras

model_path = "C:\\Users\\JyunmauChan\\Documents\\GitHub\\IMG-REC\\Models\\cifar10_ResNet20v1_model.045.h5"


class ImageRecognition(object):
    def __init__(self):
        self.model = keras.models.load_model(model_path)
        self.category = ["airplane", "automobile", "bird", "cat",
                         "deer", "dog", "frog", "horse", "ship", "truck"]

    def image_predict(self, img):
        np_img = self._qimg2mat_format(img)
        y = self.model.predict(np.array([np_img]))
        _, cate_index = np.where(y == np.max(y, axis=1))
        print(self.category[cate_index[0]])

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
