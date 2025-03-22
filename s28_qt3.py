from PyQt5.QtWidgets import QApplication, QWidget
# from s27_qt2 import MyWindow
from s28_qt3ui import Ui_Form
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot

ownd, ocls = uic.loadUiType('s28_qt3.ui')

#class MyWindow(QWidget, Ui_Form):
class MyWindow(ocls, ownd):
    counter = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # on_ObjetName_signal(self, ....)
    @pyqtSlot()
    def on_pb1_clicked(self):
        print('Button 1 clicked')
        self.counter = self.counter + 1
        self.lb1.setText(f'Our counter is {self.counter}')

app = QApplication([])
wnd = MyWindow()
wnd.show()
app.exec()
