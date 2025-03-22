class SomeClass:
    def __init__(self, war1=0, war2=0):
        print(f'Init with {war1} {war2}')
        self.atr1 = war1
        self.atr2 = war2
        
    def show(self):
        print(f'Attrs: {self.atr1}, {self.atr2}')
        
    def __str__(self):
        return f'My attributes {self.atr1}, {self.atr2}'
    
    def __repr__(self):
        return f'SomeClass({self.atr1}, {self.atr2})'
    
sc1 = SomeClass()
sc2 = SomeClass(3)

sc2.show()

print(sc2)
print(sc1)
sc3 = SomeClass(345, 1232)
print(sc3)

print(str(sc3))
mystr = f'obj; {sc1} ob2: {sc2} ob3: {sc3}'
print(mystr)

myoblist = [sc1, sc2, sc3]
for nr, o in enumerate(myoblist):
    print(nr, o)
    
print(myoblist)




