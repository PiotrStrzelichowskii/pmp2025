class First:
  atrf1 = 3
  def method1(self):
    print('method 1 in first')
  
  def method2(self):
    print('method 2 in first')

  def method4(self, a):
    print('method 4 in first')
    self.atrf1 = a

class Second(First):
  atrs1 = 6
  atrf1 = 7
  def method3(self):
    print('method 3 in second')

  def method2(self):
    print('Modified method 2 in second')
  
  def method1(self):
    #First.method1(self)
    super().method1()
    print('New functionality in method 1 in Sec') 

  def __str__(self):
    return f'{self.atrf1}, {self.atrs1}'
  
  def method4(self, na):
    #print('method 4 in Second')
    #self.atrf1 = na
    # First.method4(self, na)
    super().method4(na)
    print('New functionality [na*2] to atrs1')
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