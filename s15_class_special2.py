class Number:
    def __init__(self, n):
        self.n = n
        
    def __str__(self):
        return f'{self.n}'
    
    def __repr__(self):
        return f'Number({self.n})'
    
    #def __add__(self, something):
     #   print('Self in add:', self)
      #  print('Something in add:', something)
       # result = self.n + something.n
        #return Number(result)
    
    def __add__(self, other):
        if isinstance(self,Number) and isinstance(other,Number):
            return Number(self.n + other.n)
        else:
            print('Object not supported')
            
            
    def __sub__(self, other):
        return Number(self.n - other.n)
        
n = Number(4)
print(n)

n1 = Number(2)
print(n1)
n2 = Number(5)
print(n2)

my1 = [n1, n2, n1]
print(my1)

#print(n1 + n2)
n3 = n1 + n2
print(n3)

print(n3 + n1)
n4 = n3 + n1 + n2

n6 = n2 - n1