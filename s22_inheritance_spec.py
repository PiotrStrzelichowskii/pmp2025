class Mother:
  def __init__(self, a, b):
      self.m1 = a
      self.m2 = b

  def __repr__(self):
      return f'Mother({self.m1}, {self.m2})'
  
class Child(Mother):
  def __init__(self, a1, a2, a3 = 'Empty'):
      #Mother.__init__(self, a1, a2)
      super().__init__(a1, a2)
      self.name = a3

  def makesum(self):  
    result = self.m1 + self.m2
    self.m3 = result
    return result
  
  def __str__(self):
    return f'Child({self.m1}, {self.m2}, {self.name})'
  
  def __repr__(self):
    frommother = super().__repr__()
    result = f'Child {frommother[6:-1]},{self.name})'
    return result


co1 = Child(3, 6.21)
print(co1)
res = co1.makesum()
print(res)
print(co1.m3)

co2 = Child(4, 7.21, 'Tom')
print(co2)

mylist = [co1, co2]
print(mylist)