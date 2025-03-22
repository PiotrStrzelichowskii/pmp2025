class One:
    def __init__(self):
        super().__init__()
        print('init 1')
    def one(self):
        print('method one')
    def show(self):
        print('Show from one')
class Two:
    def __init__(self):
        super().__init__()
        print('init 2')
    def two(self):
        print('method two')
    def show(self):
        print('Show from second')
class Three:
    def __init__(self):
        super().__init__()
        print('init 3')
    def three(self):
        print('method theee')
    def show(self):
        print('Show from three')

class MyClass(One, Two, Three):
    def __init__(self):
        super().__init__()
        #
        #Two.__init__(self)
        #Three.__init__(self)


mc1 = MyClass()
mc1.one()
mc1.two()
mc1.three()
mc1.show()
print(MyClass.__mro__)

from s23_inher_multi import First, Second, Third

class SomeCLass(Third, One, Second, Two, First):
    pass

sc1 = SomeCLass()
print(SomeCLass.__mro__)