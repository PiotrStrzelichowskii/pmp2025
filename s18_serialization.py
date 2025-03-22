mydict = {
    'some list': [4,3,6,7],
    'some other dict': {'v1': 6, 'v3':8, 'v1':9},
    'tuple': (4, 'kkk', 6.253, 'bbb')
    }

mylist = [4, 3, 6, 7]
with open('numbers.txt', 'w') as file:
    for v in mylist:
        file.write(f'{v} ')

newlist = []
with open('numbers.txt') as file:
    for s in file.read().split(' ')[:-1]:
        newlist.append(int(s))
print(newlist)

import json

with open('number.json', 'w') as file:
    json.dump(mylist, file)
    
with open('number.json', 'r') as file:
    #print('From json:', json.load(file))
    newlist = json.load(file)
print(newlist)

with open('mydict.json', 'w') as file:
    json.dump(mydict, file, indent=4)

with open('mydict.json', 'r') as file:
    newdict = json.load(file)
print(newdict)

class MyClass:
    first = 1
    second = 4.3847
    thrid = 'Ala ma kota'
    def method(self):
        print(self.first, self.second, self.thrid)

mo1 = MyClass()
mo1.method()

# with open('myclass.json', 'w') as file:
#     json.dump(mo1, file)  # this would need implementation of special method in our class

import pickle

with open('myclass.pkl', 'wb') as file:
    pickle.dump(mo1, file)

with open('myclass.pkl', 'rb') as file:
    mno1 = pickle.load(file)


print(mno1)
mno1.method()