from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, QTimer
import time
import random

ui, mwnd = uic.loadUiType('s35_progress.ui')

class MyWindow(mwnd, ui):
  range = 0
  id = 0
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    print('Progressbar on start:',self.progressBar.value())

    self.timer = QTimer()
    self.timer.setInterval(500)
    self.timer.timeout.connect(self.run_on_timer)
    self.timer.start()


  def add_to_table(self, myid, myts, mynr):
    print('Adding to table:', myid, myts, mynr)

    self.twOur.insertRow(0)
    ti1 = QTableWidgetItem(f'{myid}')
    ti2 = QTableWidgetItem(f'{myts}')
    ti3 = QTableWidgetItem(f'{mynr}')

    self.twOur.setItem(0, 0, ti1)
    self.twOur.setItem(0, 1, ti2)
    self.twOur.setItem(0, 2, ti3)

    self.twOur.resizeColumnsToContents()


  def run_on_timer(self):
    print('Timer')
    ev = self.pbTime.value()
    self.pbTime.setValue(ev+1)
    ts = time.time()
    self.id = self.id + 1
    nr = random.randint(1,100)
    self.add_to_table(self.id, ts, nr)

  def calculate(self):
    step = int(100/self.range)
    for v in range(self.range):
      time.sleep(0.1)
      #self.progressBar.setValue(v)
      self.progressBar.setValue(int(v*step))
    self.progressBar.setValue(100)

  def on_dial_valueChanged(self, val):
    #self.progressBar.setValue(val)
    self.range = val

  @pyqtSlot()
  def on_pbCalc_clicked(self):
    self.calculate()

if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()