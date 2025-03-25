from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

ui, mwnd = uic.loadUiType('s30_text.ui')

class MyWindow(mwnd, ui):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    #self.lbAlice.setText('Tom has a dog')

  def on_pbCAlice_pressed(self):
    self.lbAlice.setText('Pushbutton was pressed')


  def on_pbCAlice_released(self):
    self.lbAlice.setText('Alice has a cat')

  def on_leMyText_textChanged(self, something):
    print('Text changed:', something)
  
  def on_leMyText_returnPressed(self):
    print('Return')
    ct = self.leMyText.text()
    print(f'Current text: {ct}')

  @pyqtSlot()
  def on_pbClear_clicked(self):
    self.leMyText.setText('')


if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()