from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

ui, mwnd = uic.loadUiType('ex7.ui')

class MyWindow(mwnd, ui):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

  @pyqtSlot()
  def on_pb1_clicked(self):
    print('Button pb1 clicked')
    self.cb1.toggle()
    self.cb2.toggle()
    self.cb3.toggle()

  @pyqtSlot()
  def on_pb2_pressed(self):
    print('Button pb2 pressed')
    cb1_state = self.cb1.isChecked()
    cb2_state = self.cb2.isChecked()
    cb3_state = self.cb3.isChecked()
    
    if cb1_state == cb2_state == cb3_state == False:
      self.cb1.setChecked(True)
    elif cb1_state:
        self.cb1.setChecked(False)
        self.cb2.setChecked(True)
    elif cb2_state:
        self.cb2.setChecked(False)
        self.cb3.setChecked(True)
    elif cb3_state:
        self.cb3.setChecked(False)
        self.cb1.setChecked(True)

  def on_cb1_toggled(self, var):
      print('Checkbox cb1 toggled', var)

  def on_cb2_stateChanged(self, var):
      print('Checkbox cb2 state changed', var)

  def on_cb3_toggled(self, var):
      print('Checkbox cb3 toggled', var)

  def on_rb1_toggled(self, var):
     print('Radio button rb1:', var)

  def on_rb2_toggled(self, var):
    print('Radio button rb2:', var)

  def on_rb3_toggled(self, var):
     print('Radio button rb3:', var)

  def on_rb4_toggled(self, var):
     print('Radio button rb4:', var)

  def on_pb3_released(self):
    print('Button pb3 released')
    if self.rb1.isChecked():
        self.rb2.setChecked(True)
    elif self.rb2.isChecked():
        self.rb1.setChecked(True)
    
    if self.rb3.isChecked():
        self.rb4.setChecked(True)
    elif self.rb4.isChecked():
        self.rb3.setChecked(True)


if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()


