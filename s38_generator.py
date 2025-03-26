from sys import getsizeof as size 

for i in [2,4,8,16,32,64,128,256,512,1024]:
  print(i, end = ' ')
print()

def squareof2():
  sq = []
  for i in range(200):
    sq.append(i*i)
  return sq

#for i in squareof2():
#  print(i, end = ' ')
#print()

print(size(squareof2()))

#def squareof2gen():
#  i=2
#  while True:
#    retval = i*2
#    i = i + 2
#    return retval
#  
#print(squareof2gen())
#print(squareof2gen())  
#for v in squareof2gen():
#  print(v)

def squareof2gen():
  i=2
  while True:
    retval = i*2
    i = i + 2
    yield retval

gen = squareof2gen()
print('Size of generator:', size(gen))

print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
  print(i, end=' | ')
  if i > 100000:
    break
print()

def order():
  print('Do this first')
  yield 'done first'
  print('Do this second')
  yield 'done second'
  print('Do this third')
  yield 'done third'

genorder = order()

print(next(genorder))
print(next(genorder))
print(next(genorder))

mylist = [i*2 for i in range(10)]
print(mylist)

mygen = (i*2 for i in range(10))
print(mygen)