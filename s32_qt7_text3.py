from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot

ui, mwnd = uic.loadUiType('s32_menus.ui')

class MyWindow(mwnd, ui):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle('Menu example')
    self.statusBar().showMessage('Our program is starting', 3000)

  @pyqtSlot()
  def on_actionOpen_triggered(self):
    print('Open app')
    filename, flt = QFileDialog.getOpenFileName()
    print(filename, flt)
    with open(filename, 'r') as file:
      print(file.read())

  def on_actionSave_triggered(self):
    print('Save app')
    filename, flt = QFileDialog.getSaveFileName()
    print(filename, flt)


  @pyqtSlot()
  def on_actionExit_triggered(self):
    print('Exit app')
    answer = QMessageBox.question(self, 'Exit', 'Do you really want to exit?')
    if answer == QMessageBox.Yes:
      exit()
    else:
      pass

  @pyqtSlot()
  def on_actionAbout_triggered(self):
    print('About app')
    QMessageBox.about(self, 'About program', 'This is a simple program')

  @staticmethod
  def this_is_my_static():
    print('I am in static method')

if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    wnd.this_is_my_static()
    MyWindow.this_is_my_static()
    app.exec()