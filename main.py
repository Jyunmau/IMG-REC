import sys

from PySide2 import QtWidgets

from Core.CameraMainWin import CameraMainWin
from Core.ResultWid import ResultWid
from Core.ImageRecognition import ImageRecognition
from Core.SingleResultWid import SingleResultWid


def main():
    app = QtWidgets.QApplication(sys.argv)
    image_recognition = ImageRecognition()
    result_wid = ResultWid(image_recognition)
    single_result_wid = SingleResultWid(image_recognition)
    camera_main_win = CameraMainWin(image_recognition, result_wid, single_result_wid)
    camera_main_win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
