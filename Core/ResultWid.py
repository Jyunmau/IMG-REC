from PySide2 import QtWidgets
import Qt_Ui.ui_resultWid as ui_resultWid


class ResultWid(QtWidgets.QWidget, ui_resultWid.Ui_Form):
    def __init__(self):
        super(ResultWid, self).__init__()
        self.setupUi(self)
