class MyClass:
    def __str__(self):
        return 'Tom has a dog.'

file = open('ourfile.txt','w')
print(file, type(file))
file.write('Alice has a cat')
file.write('\n')
mc1 = MyClass()
file.write(str(mc1))
file.close()

#input('Do you want to exit?')
file = open('ourfile.txt', 'r')
data = file.read()
print(data)
file.close()

file = open('ourfile.txt', 'a')
file.write('\nAnother brick in the wall.')
file.write('\nand yet another line.')
file.close()

with open('ourfile.txt') as file:
    for line in file:
        print(line, end='|')

with open('ourfile.txt', 'w') as file:
    file.write('Stuff in conext manager.\n')
    file.write('Another line inj context manager\n')
    file.write('comntext manager\n')

#input('Do you want to exit?')
with open('ourfile.txt', 'a') as file:
    file.write('THis is from append.')