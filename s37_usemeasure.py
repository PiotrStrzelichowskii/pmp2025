import time
from s36_decorator import measuretime

@measuretime
def takesometime():
  print('Start')
  time.sleep(3)
  print('End')

@measuretime
def caluculate():
  for i in range(100000):
    k = i * i

takesometime()
caluculate()