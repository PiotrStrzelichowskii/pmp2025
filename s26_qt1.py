import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

app = QApplication([])
win = QMainWindow()
win.setGeometry(100,100,600,400)
label = QLabel('My label', parent=win)
pb = QPushButton('My Button', parent=win)
pb.setGeometry(100, 100, 100, 30)

win.show()
app.exec()



# import tqdm
# import time

# for i in tqdm.tqdm(range(100)):
#     time.sleep(0.1)
#    # print(i, end='|')
#     a = 10*i

