class MyBase:
    num = 6
    flo = 4.283
    mystr = 'Alice has a cat'
    def show(self):
        print(f'{self.num} {self.flo} {self.mystr}')

    def setvals(self, a, b, c):
        self.num = a
        self.flo = b
        self.mystr = c

    def __str__(self):
        return f'From str: {self.num} {self.mystr} {self.flo}'

mb1 = MyBase()
mb1.show()


class NewClass(MyBase):
    newn = 10
    newf = 4.283
    def othershow(self):
        print(f'{self.newn} {self.newf}')


nc1 = NewClass()
print('testing new class', nc1.num, nc1.flo, nc1.mystr)
nc1.show()
nc1.setvals(7, 2.3746, "Tom has a dog")
nc1.show()
print(nc1)

print('New stuff added:', nc1.newn, nc1.newf)
nc1.othershow()