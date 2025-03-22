class PiotrOb:
    def __init__(self, v1, v2):
        print(f'PiotrOb {v1} {v2}')
        self.atr1 = v1
        self.atr2 = v2
        
    def display(self):
        print(f'Current atrs: {self.atr1} {self.atr2}')
    
    def ustaw(self, v1, v2):
        print(f'Setting atributes')
        self.atr1 = v1
        self.atr2 = v2
        
    def ret(self):
        return [self.atr1, self.atr2]
    
class StrzelichowskiOb:
    def __init__(self, *v):
        print(f'StrzelichowskiOb {v}')
        self.atr1 = None
        self.atr2 = None
        
    def display(self):
        print(f'Current atrs: {self.atr1}, {self.atr2}')
        
    def ustaw(self, v1, v2):
        print(f'Setting attributes with limit 0-10')
        if (v1 >= 0 and v1 <= 10) and (v2 >= 0 and v2 <= 10):
            self.atr1 = v1
            self.atr2 = v2
        else:
            print('Values are not from 0 to 10')
            
        
        
    def ret(self):
        return [self.atr1, self.atr2]
    
        
    
ob1 = PiotrOb(3,5)
ob1.display()
ob1.ustaw(7,2)
ob1.display()
values = ob1.ret()
print(values)


ob2 = StrzelichowskiOb()
ob3 = StrzelichowskiOb(2,7)

ob2.display()
ob3.display()

ob2.ustaw(7,2)
ob2.display()

ob2.ustaw(11,2)
ob2.display()
ob2.ret()


