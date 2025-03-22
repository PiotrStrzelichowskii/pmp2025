class First:
    def __init__(self):
        print('initializing First')
    def meth1(self):
        print('method in first')

class Second(First):
    def __init__(self):
        super().__init__()
        print('initializing Second')
    def meth2(self):
        print('method in second')

class Third(Second):
    def __init__(self):
        super().__init__()
        print('Initializing Third')
    def meth3(self):
        print('metod in third')

class MyClass(Third):
    def meth1(self):
        super().meth1()
        print('New stuff form myclass')

mc1 = MyClass()
mc1.meth3()
mc1.meth2()
mc1.meth1()
