import time

def measuretime(funkob):
  def insidedecor(*args, **kwargs):
    start = time.perf_counter()
    result = funkob(*args, **kwargs)
    end = time.perf_counter()
    print(f'Function execution time: {end-start}')
    return result
  return insidedecor


def ourdecorator(funkob):
  print('Inside decorator: ', funkob)
  def insidedecor(*ia, **ib):
    print('Inside insidedecor: ', ia, ib)
    result = funkob(*ia, **ib)

    return result
  return insidedecor


@ourdecorator
def somefunc():
  print('Somefunc')

@ourdecorator
def otherfunk(a):
  print(f'Otherfunk with {a}')

@ourdecorator
def twofunk(a, b):
  print(f'Twofunk with {a}')

@ourdecorator
def threefunk(a, b, c=0):
  print(f'Threefunk with {a}')

@ourdecorator
def getsomething():
  return 10


somefunc()
otherfunk(9)
twofunk(9, 8)
threefunk(9, 8, c=7)
ret = getsomething()
print('Returned:', ret)