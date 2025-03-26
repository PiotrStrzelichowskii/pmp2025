a = 10
b = 'a'

try:
  result = a/b
except ZeroDivisionError:
  print("Division by zero")
except TypeError:
  print("An error occurred")
else:
  print(result)
finally:
  print("This is always executed")
print("Rest of the program")


try:
  file = open('someTextfile.txt')
except FileNotFoundError:
  print("File not found")
else:
  print(file.read())
  file.close()


try:
  file = open('someTextfile.txt', 'w')
except Exception as val:
  print(f'Exception happened: {val}')
else:
  file.write('Hello, World!')
  file.close()