import sys

def process_options(opt1, opt2, opt3):
    if opt1:
        print("Option 1 activated")
    if opt2:
        print("Option 2 activated")
    if opt3:
        print("Option 3 activated")

myArgs = sys.argv

opt1 = False
opt2 = False
opt3 = False

for arg in myArgs:
    if arg == 'opt1':
        opt1 = True
    elif arg == 'opt2':
        opt2 = True
    elif arg == 'opt3':
        opt3 = True
    elif arg == 'otheropt':
        print('Another option activated')
    elif arg == 'extraopt':
        print('Extra option activated')
    

process_options(opt1, opt2, opt3)





