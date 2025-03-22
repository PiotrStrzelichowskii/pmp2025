print('Progargs')

import sys

myArgs = sys.argv

for arg in myArgs:
    if arg == 'myopt1':
        print('Option 1 activated')
    if arg == 'otheropt':
        print('Another option activated')

