class myClass:
    def __init__(self):
        print(f'Initializing myClass')

mc1 = myClass()
print(f'Reference in main: {mc1}')
mc2 = myClass()
print(f'Reference in main: {mc2}')

class myOther:
    def __init__(self,number):
        print(f'Initializing myOther class: {self} nr: {number}')
        
mo1 = myOther(5)
mo2 = myOther('Ala')
mo3 = myOther(4.213)

class myThree:
    #atr1 = 0
    #atr2 = 0
    #atr3 = 0
    
    def __init__(self,a,b,c):
        print(f'myThree {a} {b} {c}')
        self.atr1 = a
        self.atr2 = b
        self.atr3 = c
        
    def show(self, name):
        print(f'Current atrs: {name} {self.atr1} {self.atr2} {self.atr3}')
        
    def set(self, s1, s2, s3):
        print(f'Setting atributes')
        self.atr1 = s1
        self.atr2 = s2
        self.atr3 = s3
    
    def get(self):
        return self.atr1, self.atr2, self.atr3
        
mt1 = myThree(3,8,2)
mt2 = myThree(1,7,3)
mt1.show('mt1')
mt2.show('mt2')
mt1.set(4,2,0)
mt1.show('mt1 after set')
mt2.set(43, 213, 3213)


vals = mt1.get()
print(vals)

#mt3 = myThree(*mt1.get())
mt3 = myThree(*vals)