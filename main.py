import sys

from PySide2 import QtWidgets

from Core.CameraMainWin import CameraMainWin
from Core.ResultWid import ResultWid
from Core.ImageRecognition import ImageRecognition

def main():
    app = QtWidgets.QApplication(sys.argv)
    I = ImageRecognition()
    W = CameraMainWin(I)
    Y = ResultWid()
    W.reconitionButton.clicked.connect(Y.show)
    W.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
