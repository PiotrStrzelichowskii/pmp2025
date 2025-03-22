a = 1 
b = 8.432
c = 'Alice has a cat'
print(a, b, c)

# %

ourStr = 'number: %d float: %f string: %s' % (5, 3.14, 'Tomek')
print(ourStr)

ourStr = 'number: %d float: %f string: %s' % (a, b, c)
print(ourStr)

#format()
ourStr = 'number: {} float: {} string: {}'.format(a, b, c)
print(ourStr)
ml = [4, 7, 2]
ourStr = 'num1: {} num2: {} num3: {}'.format(ml[0], ml[1], ml[2])
print(ourStr)
ourStr = 'num1: {} num2: {} num3: {}'.format(*ml)
print(ourStr)

md = {'k4': 7, 'k1': 8, 'k2': 18}
ourStr = 'num1: {} num2: {} num3: {}'.format(md['k2'], md['k4'], md['k1'])
print(ourStr)
ourStr = 'num1: {k2} num2: {k4} num3: {k1}'.format(**md)
print(ourStr)


ourStr = 'num1: {a} num2: {b} num3: {c}'.format(**locals())
print(ourStr)

# f strings 
ourStr = f'num1: {a} num2: {b} num3: {c}'
print(ourStr)

# excape sequences
ourStr = 'Alice\nhas\ta\n\tcat'
print(ourStr)

print('alice has a cat'.capitalize())
print('alice has a cat'.upper())
