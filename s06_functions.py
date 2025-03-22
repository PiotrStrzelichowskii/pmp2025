def funk1():
    print('our funk1')
    print('another line in funk1')
    
funk1()

def funk2(var1, var2):
    print(f'var1 {var1} var2 {var2}')
    
funk2(2, 4)

def funk3(v3, v1, v2):
    print(f'{v1}, {v2}, {v3}')
    
funk3(3,5,6)
funk3(1,2,3)

def funk4(val1, val2):
    print(f'{val1}, {val2}')
    oursum = val1 + val2
    return oursum

res = funk4(2,4)
print(res, id(res))

def funk5(x = 0, y = 9, z = 0):
    print(f'{x} {y} {z}')
    
funk5(5, 2, 7)
funk5(2, 5)
funk5(6)
funk5()

funk5(z=6)
funk5(y=1, x=10)

def funk6(a,b,c):
    return a+2, b+2, c+3

vals = funk6(3,8,1)
print(vals)
