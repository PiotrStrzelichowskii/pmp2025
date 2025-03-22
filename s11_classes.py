class myClass:
    pass

mo1 = myClass()
print(mo1)
print(hex(id(mo1)))

mo1.myatr1 = 7
print(mo1.myatr1)
mo1.myatr2 = 4.32
mo1.myatr3 = 'string'

mo2 = myClass()
print(mo2)
mo2.myatr1 = 2
mo2.myatr2 = 6.14
mo2.myatr3 = 'Alix'

print('Atrs in first obj')
print(mo1.myatr1)
print(mo1.myatr2)
print(mo1.myatr3)

