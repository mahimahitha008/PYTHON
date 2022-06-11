'''  #1
import math
print(math.pi)
print(math.ceil(9.8))
help(math)    #that helps us to know usage of the module
print(dir(math))     #specified module display
print(dir())     #current display module using functions
'''
'''   #2
import math as tham
print(tham.pi)
print(tham.ceil(9.7))
print(tham.sqrt(16))
'''
''' #3
from math import *
print(pi)
print(ceil(9.7))
print(sqrt(16))
'''
from math import pi as ip,ceil as liec
print(ip)
print(liec(9.7))
print(sqrt(16))    #it wont execute as it is not defined

