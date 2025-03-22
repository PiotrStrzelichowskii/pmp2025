print(0,1, type(0), type(1))
print(False,True, type(False), type(True))

# ==, !=, <, >, <=, >=

print(6 == 7)
print( 6 < 7)

# and, or, not

print((10 == 10) and (7 < 10))
print((7 > 3) or (1!=1))
print(not (True or True))

if True:
    print('Condition was true')
    
if False:
    print('aaaaaaaaaaaaa')
    
var = 9

if (var == 10):
    print('var was 10')
elif (var == 9):
    print('var is 9')
elif (var > 100):
    print('Var is greater than 100')
else:
    print('Something else')
    
    
inp = input()
print(inp, type(inp))

inp = int(inp)

if inp != 7:
    print('you entered something else')