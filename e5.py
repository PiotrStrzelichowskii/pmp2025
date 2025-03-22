import json
import pickle

#Create own class with at least 3 atributes and implement various special functions for it.
#Use comparison, arithmetic operations, representation.
#Use all file operations (json, pickle, text file) to store and read your objects to and from disk.


class Mathematical:
    def  __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'All atributes: {self.a} {self.b} {self.c}'

    def __add__(self):
        result =  self.a + self.b + self.c
        return f'Sum: {result}'
    
    def __sub__(self):
        result = self.a - self.b - self.c
        return f'Substraction: {result}'
    
    def __eq__(self, other):
      return self.a == other.a and self.b == other.b and self.c == other.c

    def __lt__(self, other):
      return (self.a + self.b + self.c) < (other.a + other.b + other.c)

    def __mul__(self, other):
      return (self.a * other.a, self.b * other.b, self.c * other.c)

    def __repr__(self):
      return f'Mathematical(a={self.a}, b={self.b}, c={self.c})'
    
    #####
    def mathematical_to_json(self):
      return {'a': self.a, 'b': self.b, 'c': self.c}

    @staticmethod
    def json_to_mathematical(data):
      return Mathematical(data['a'], data['b'], data['c'])




m1 = Mathematical(3)
print(m1.__str__())
m2 = Mathematical(3, 4, 6)
print(m2.__str__())
print(m2.__add__())
print(m2.__sub__())

# New methods
m3 = Mathematical(3, 4, 6)
print(f"m2 == m3: {m2 == m3}")
print(f"m1 < m2: {m1 < m2}")
print(f"m2 * m3: {m2 * m3}")
print(repr(m2))
print()

# Text file 
with open('mathematical.txt', 'w') as file:
  file.write(m2.__str__())

with open('mathematical.txt', 'r') as file:
  txt_data = file.read()
print(f"Read from text file: {txt_data}")

# JSON 

with open('mathematical.json', 'w') as file:
  json.dump(m2.mathematical_to_json(), file)

with open('mathematical.json', 'r') as file:
  json_data = m2.json_to_mathematical(json.load(file))
print(f"Read from JSON: {json_data}")

# Picklee

with open('mathematical.pkl', 'wb') as file:
  pickle.dump(m2, file)

with open('mathematical.pkl', 'rb') as file:
  pickle_data = pickle.load(file)
print(f"Read from pickle: {pickle_data}")