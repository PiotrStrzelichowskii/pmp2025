class MyNum(int):
    def double(self):
        return self*2

a = MyNum(3)
b = MyNum(5)
print(a, b)
c = a + b
print(c)
d = c+a
print(d)
print(a.double())

class MyStr(str):
    pass

s1 = 'My string'
s2 = 'Other string'
print(s1.upper() + s2)
