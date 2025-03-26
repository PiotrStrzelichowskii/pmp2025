from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot
import os

ui, mwnd = uic.loadUiType('ex8.ui')

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

    if Name == '':
      QMessageBox.warning(self, 'Warning', 'You need to type filename!')
    elif not Name.endswith('.txt'):
      QMessageBox.warning(self, 'Warning', 'File must have .txt extension!')
    elif not os.path.exists(Name):
      QMessageBox.warning(self, 'Warning', 'File does not exist!')
    else:
      with open(Name, 'r') as f:
        self.ptOurs.setPlainText(f.read())
       

  def on_leName_returnPressed(self):
    print('Return')
    Name = self.leName.text()
    print(f'Current text: {Name}')
    return Name
  
  @pyqtSlot()
  def on_actionOpen_triggered(self):
    print('Open app')
    filename, flt = QFileDialog.getOpenFileName()
    print(filename, flt)
    with open(filename, 'r') as file:
      content = file.read()
      print(content)
      self.ptOurs.setPlainText(content)

  @pyqtSlot()
  def on_actionSave1_triggered(self):
    print('Save app')
    content = self.ptOurs.toPlainText()
    filename, flt = QFileDialog.getSaveFileName()
    print(filename, flt)
    if filename:
        with open(filename, 'w') as f:
            f.write(content)


  @pyqtSlot()
  def on_actionExit_triggered(self):
    print('Exit app')
    answer = QMessageBox.question(self, 'Exit', 'Do you really want to exit?')
    if answer == QMessageBox.Yes:
      exit()
    else:
      pass



if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()