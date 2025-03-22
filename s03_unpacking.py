a = 6
a, b = tuple((int(3), int(8)))
print(a, b)

a, b, c = 5, 8, 2
print(a, b, c)

myList = [4, 7, 2, 6, 8, 7, 2]
a, b, c, *d = myList
print(a, b, c, d)

*d, a, b, c = myList
print(a, b, c, d)


a, *d, b, c = myList
print(a, b, c, d)