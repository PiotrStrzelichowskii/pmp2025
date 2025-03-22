def funka(a, b ,c):
    print(f'from list: {a} {b} {c}')
    
funka(5,2,7)

myList = [9,1,3]
funka(myList[0], myList[1], myList[2])
funka(*myList)

def funkb(a, b ,c, *d):
    print(f'from list: {a} {b} {c}')
    print(d)

myList2 = [5,1,6,6,1,7,2]

funkb(*myList2)

def funkc(*v):
    print(v)
    
funkc(6,7,8)

myDict = {'k7':4, 'k2':9, 'k1':3, 'k9':2}

def funkd(a,b,c,d):
    print(a,b,c,d)
    
funkd(myDict['k7'], myDict['k2'], myDict['k1'], myDict['k9'])

def funkd1(**mys):
    print(mys)

funkd1(**myDict)

def funkd2(k1, k2, k7, k9):
    print(k1, k2, k7, k9)

funkd2(**myDict)

def funkd3(**myd):
    print(myd)

funkd2(k9=2, k7=3, k1=1, k2=5)
    
def funku(*a, **b):
    print(a, b)
    
funku(3, 7, 3)
funku(k=2, z=8)
funku(3, 8, l=1, k=9)

def someFunction(*args, **kwargs):
    pass