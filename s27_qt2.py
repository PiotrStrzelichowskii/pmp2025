from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget

class MyWindow(QWidget):
    counter = 0
    def __init__(self):
        super().__init__()
        self.setui()

    def clicked_pb1(self):
        print('Clicked pb1')
        print(self.lb1)
        self.counter = self.counter + 1
        self.lb1.setText(f'New text {self.counter}')

    def clicked_pb2(self):
        print('Clicked pb2')
        self.counter = self.counter + 1
        self.lb2.setText(f'Sec text {self.counter}')


    def setui(self):
        self.setGeometry(100, 100, 600, 400)
        self.lb1 = QLabel('Our label in window', parent=self)
        pb1 = QPushButton('Our Button', parent=self)
        pb1.setGeometry(100,100, 100, 30)

        self.lb2 = QLabel('Second label in window', parent=self)
        self.lb2.setGeometry(200, 10, 200, 20)
        pb2 = QPushButton('Sec Button', parent=self)
        pb2.setGeometry(200,100, 100, 30)

        pb1.clicked.connect(self.clicked_pb1)
        pb2.clicked.connect(self.clicked_pb2)

if __name__=="__main__":
    app = QApplication([])
    wnd = MyWindow()
    #wnd.setui()
    wnd.show()
    app.exec()