#Create your own package that will contain at least 2 modules. 
# Each module shold have at leat 3 funtions that have different kinds of paramerters(positional, default).  
# Funtion calls should be a mix of straight arguments but also list and dict unpacking result.
#Functions should use coditionals, loops, slicing and other stuff that we used during class.
#One fuunction shoud search for a vaue inside a tuple.

from mypacage.module1 import fun1, fun2, fun3
from mypacage.module2 import func1, func2, func3, func4

fun1(2, 5, 8)
print(fun2())
print(fun2(3,4,5))
fun3()

func1('Tomek has a monkey')
func2([4,5,8,2,5,3])
print()
print(func3(*[4,5,8,2,5,3]))

myTuple = (1, 2, 3, 4, 5)
print(func4(3, myTuple))
print(func4(10, myTuple))
    
