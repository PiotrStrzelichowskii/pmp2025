class Another:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        if self.val == other.val:
            return True
        else:
            return False

    def __eq__(self, other):
        return (self.val == other.val)

    def __gt__(self, other):
        if self.val > other.val:
            return True
        else:
            return False

a1 = Another(7)
a2 = Another(5)

# print(5 == 7)
# v1 = 5
# v2 = 7
# print(v1 == v2)

print('a1 == a2', a1 == a2)
print('a1 != a2', a1 != a2)

a3 = Another(7)
print('a3 == a1', a3 == a1)
print('a3 == a1', a3 != a1)

print('a1 > a2', a1 > a2)
print('a2 > a3', a2 > a3)

print('a2 < a3', a2 < a3)


class Double:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __eq__(self, other):
        if self.v1==other.v1 and self.v2==other.v2:
            return True
        else:
            return False
d1 = Double(3, 2)
d2 = Double(2, 9)
print(d1 == d2)
print(d1 != d2)
d3 = Double(3, 2)
print(d1 == d3)
print(d1 != d3)
d4 = Double(3, 'Tom')
d5 = Double(3, 'Tom')
print(d4 == d5)

