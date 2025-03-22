string = 'I have cats and they are year old.'
a = 2
b = 1.5
c = 'They are cute.'
ml = [2, 1.5, 'They are cute.']

md = {'k1': 7, 'k2': 8.5, 'k3': 'Its not enough :)'}

# %
string = 'I have %d cats and they are %f years old. %s' % (2, 1.5, 'They are cute.')
print(string)
string = 'I have %d cats and they are %f years old. %s' % (a,b,c)
print(string)

#format()

string = 'I have {} cats and they are {} years old. {}'.format(a,b,c)
print(string)
string = 'I have {} cats and they are {} years old. {}'.format(a,b,c)
print(string)
string = 'I have {} cats and they are {} years old. {}'.format(ml[0], ml[1], ml[2])
print(string)
string = 'I have {} cats and they are {} years old. {}'.format(*ml)
print(string)


string = 'I have {} cats and they are {} years old. {}'.format(md['k1'], md['k2'], md['k3'])
print(string)
string = 'I have {k1} cats and they are {k2} years old. {k3}'.format(**md)
print(string)

string = 'I have {a} cats and they are {b} years old. {c}'.format(**locals())
print(string)


#f string
string = f'I have {a} cats and they are {b} years old. \n {c}'
print(string)