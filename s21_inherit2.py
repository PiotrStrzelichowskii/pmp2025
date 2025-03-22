class First:
    atrf1 = 3
    def method1(self):
        print('method 1 in First')
    def method2(self):
        print('method 2 in First')

    def method4(self, a):
        print('Print method4 in First')
        self.atrf1 = a

class Second(First):
    atrs1 = 6
    atrf1 = 10
    def method3(self):
        print('method 3 in Second')
    def method2(self):
        print('modified method 2 in Second')
    
    def method1(self):
        # print('method 1 in First')
        #First.method1(self)
        super().method1()
        print('New functionality in method1 in Sec')

    def __str__(self):
        return f'{self.atrf1} {self.atrs1}'

    def method4(self, na):
        # print('Print method4 in First')
        # self.atrf1 = na
        # First.method4(self, na)
        super().method4(na)
        print(f'New functionality {na*2} to atrs1')
        self.atrs1 = na*2

sec1 = Second()
sec1.method1()
sec1.method2()
sec1.method3()
print(sec1.atrf1, sec1.atrs1)

#First.method1(None)
#First.method1(sec1)

sec1.method4(6)
print(sec1)
