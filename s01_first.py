print('first program')

a = 5
b = 3.14
c = 'Ala ma kota'
print(a, b, c)

print(5, id(5), id(a))
print(3.14, id(3.14), id(b))
print('Ala ma kota', id('Ala ma kota'), id(c))

myList = [1, 2, 3, 4, 5]
print(myList, type(myList))
myList[2] = 1
print(myList)

myTuple = (1, 2, 3, 4, 5)
#print(myTuple, type(myTuple))
#print(myTuple)

print(myList[0], myTuple[0])

mySet = {3, 6, 2, 9, 1, 6}
print(mySet, type(mySet))
mySet.add(4)
print(mySet)

myDict = {'k7': 9, 'k1': 3, 'k5': 'Ala', 'k2': 3.14}
print(myDict, type(myDict))
print(myDict['k5'])
myDict['k5'] = 'Ola'
myDict['k6'] = 14
print(myDict)

print(myDict.get('k7'))
print(myDict.get('k9'), 'Cannot find key')
