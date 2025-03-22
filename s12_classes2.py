class myClass:
    myatr1 = 0
    myatr2 = 3.21
    myatr3 = 'haga'
    
    def someFun(something, mo1frommain):
        print(something, mo1frommain)
        
    def otherFun(self):
        print(self)
        
    def showatrs(self):
        print(f'All: {self.myatr1}, {self.myatr2}, {self.myatr3}')
        
    def setarts(self, a, b, c):
        self.myatr1 = a
        self.myatr2 = b
        self.myatr3 = c
    
mo1 = myClass()
print(mo1, type(mo1))
print(mo1.myatr1, mo1.myatr2, mo1.myatr3)

mo2 = myClass()
print(mo2, type(mo2))
print(mo2.myatr1, mo2.myatr2, mo2.myatr3)
mo2.myatr2 = 8.432

print(mo1.myatr2, mo2.myatr2)

mo1.someFun(mo1)

mo1.showatrs()
mo2.showatrs()

mo3 = myClass()
mo3.setarts(3, 3.432, 'Jake')
mo3.showatrs()
