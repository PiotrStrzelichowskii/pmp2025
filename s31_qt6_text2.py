from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

ui, mwnd = uic.loadUiType('s31_text.ui')

class MyWindow(mwnd, ui):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

  @pyqtSlot()
  def on_pbSave_clicked(self):
    ot = self.ptOurs.toPlainText()
    #print(f'Our text: {ot}')
    Name = self.on_leName_returnPressed()
    with open(Name, 'w') as f:
        f.write(ot)

  @pyqtSlot()
  def on_pbLoad_clicked(self):
    Name = self.on_leName_returnPressed()
    with open(Name, 'r') as f:
        self.ptOurs.setPlainText(f.read())

  def on_leName_returnPressed(self):
    print('Return')
    Name = self.leName.text()
    print(f'Current text: {Name}')
    return Name


if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()