from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

ui, mwnd = uic.loadUiType('s29_buttons.ui')

class MyWindow(mwnd, ui):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.pbOurs.setCheckable(True)  # Make the button checkable
    self.pbOurs.clicked.connect(self.doSomething)
    #self.pbOther.clicked.connect(self.otherMethod)

  def doSomething(self):
    print('Button clicked')

  # def on_ObjectName_signal(self, ....): #General schema for slot name

  @pyqtSlot()
  def on_pbOther_clicked(self):
    print('Other button clicked')
    self.cbSecond.toggle()

  def on_pbThird_pressed(self):
    print('Third button pressed')

  def on_pbThird_released(self):
    print('Third button released')

  def on_cbFirst_toggled(self, var):
    print('First checkbox toggled', var)

  def on_cbSecond_stateChanged(self, var):
    print('Second checkbox state changed', var)

  def on_pbOurs_toggled(self, state):
    print('Our button toggled', state)

  def on_rbFirst_toggled(self, state):
    print('First radio button toggled', state)

  def on_rbSecond_toggled(self, state):
    print('Second radio button toggled', state)

  def on_rbThird_toggled(self, state):
    print('Third radio button toggled', state)

if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()