from ex08_pizza_party.calc import *

numppl = input("How many people? ")
numpizzas = input("How many pizzas? ")
numslices = input("How many slices per pizza? ")

slicesPerPerson, slicesLeftOver = calc(numppl, numpizzas, numslices)

print("\nNumber of slices per person: {}\nNumber of slices remaining: {}\n".format(slicesPerPerson, slicesLeftOver))
