while False:
    print('this is if with jump to beginning')
    
counter = 10

while (counter > 0):
    print(f'Loop {counter}')
    print(counter % 2)
    if not counter % 2:
        counter -= 2
        
while True:
    print('Inside forever loop')
    break

for element in [3,6,8,2,3]:
    print(f'in list: {element}')
    
for val in range(10):
    print(val, end=', ')
    
print()
for val in range(4, 10):
    print(val, end=', ')
    
print()
for val in range(4, 10, 2):
    print(val, end=', ')
    
for l in 'fidsijfidsjflds':
    print(l, end=', ')
    
    
    