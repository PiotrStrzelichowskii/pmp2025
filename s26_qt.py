import PyQt5
from PyQt5.QtWidgets import QApplication, QWindow, QLabel

app = QApplication([])
win = QMainWindow()
label = QLabel('Hello World!', parent=win)
pb = QPushButton('Click me!', parent=win)
pb.setGeometry(100, 100, 50, 20)

#label.show()

win.show()
app.exec_()




#import tqdm
#import time

#for i in range(100):
#  time.sleep(0.1)