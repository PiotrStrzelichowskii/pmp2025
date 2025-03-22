import s09_myModule

print(s09_myModule.myVar)
s09_myModule.myFunk()

a = s09_myModule.myVar
b = s09_myModule.myFunk

print(a)
b()

myVar = s09_myModule.myVar
myFunk = s09_myModule.myFunk
print(myVar, myFunk)

from s09_myModule import secFunk, secVar

print(secVar)
secFunk()