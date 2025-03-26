from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

ui, mwnd = uic.loadUiType('s34_values.ui')

class MyWindow(mwnd, ui):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

  def on_hsOurs_valueChanged(self, value):
     print('Value:', value)
     self.lbHs.setText(f'{value}')
     self.sbHs.setValue(value)

  @pyqtSlot(int)
  def on_sbHs_valueChanged(self, value):
    print('Value:', value)
    self.hsOurs.setValue(value)

  def on_dial_valueChanged(self, value):
    print(value, type(value))
    self.hsOurs.setValue(value)


  def on_vsOurs_valueChanged(self, value):
     print('Value:', value)
     self.hsSb.setValue(value)
     self.vsSb.setValue(value)

  def on_hsSb_valueChanged(self, value):
     print('Value:', value)
     self.vsOurs.setValue(value)

  def on_vsSb_valueChanged(self, value):
     print('Value:', value)
     self.vsOurs.setValue(value)



if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()