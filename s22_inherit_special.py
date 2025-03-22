class Mother:
    def __init__(self, a, b):
        self.m1 = a
        self.m2 = b
    def __repr__(self):
        return f'Mother({self.m1}, {self.m2})'
    def otherfun(self):
        print('Do something else')

class Child(Mother):
    def __init__(self, a1, a2, a3="Empty"):
        #Mother.__init__(self, a1, a2)
        super().__init__(a1, a2)
        self.name = a3

    def makesum(self):
        result = self.m1 + self.m2
        self.m3 = result
        return result

    def __str__(self):
         return f'{self.m1}, {self.m2}, {self.name}'

    def __repr__(self):
        from_mother = super().__repr__()
        result = f'Child{from_mother[6:-1]}, {self.name})'
        return result
        # return f'Child({self.m1},{self.m2},{self.name})'

co1 = Child(3, 6.23)
print(co1)
res = co1.makesum()
print(res)
print(co1.m3)

co2 = Child(6, 2.273, 'Tom')
print(co2)

mylist = [co1, co2]
print(mylist)
co2.otherfun()