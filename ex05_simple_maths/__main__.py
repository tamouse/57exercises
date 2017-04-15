
from ex05_simple_maths.simple import *

x = float(input("Give me a number: "))
y = float(input("Give me another number: "))

simple = SimpleMaths(x, y)

print("x + y = {}".format(simple.add()))
print("x - y = {}".format(simple.subtract()))
print("x * y = {}".format(simple.multiply()))
print("x / y = {}".format(simple.divide()))
