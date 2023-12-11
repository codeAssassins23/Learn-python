### Modules ###
# A module is a file containing Python definitions and statements.
import my_module
from my_module import sumValues, printValue
import math
import random
# from math import pi with alias
from math import pi as PI_VALUE
print(sumValues(1 , 2, 3))
printValue("Hello world")

print(math.modf(2.5))
print(random.random())
print(math.pow(2,8))

print(PI_VALUE)