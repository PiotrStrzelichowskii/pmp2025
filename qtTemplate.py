from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

ui, mwnd = uic.loadUiType('qtTemplate.ui')

class MyWindow(mwnd, ui):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()