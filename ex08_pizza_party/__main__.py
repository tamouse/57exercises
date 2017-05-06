from ex08_pizza_party.calc import *

numppl = None
numpizzas = None
numslicesper = None
numslices = None

numppl = input("How many people? ").strip()
numpizzas = input("How many pizzas? (Press enter if you don't know) ").strip()

if numpizzas == '':
  numslicesper = input("Ok, how many slices per person, then? ").strip()
  numpizzas = None

numslices = input("How many slices per pizza? ").strip()

try:
  if numslicesper is not None:
    numPizzasNeeded, slicesLeftOver = calcPizzas(numppl, numslicesper, numslices)
    print("\nNumber of pizzas needed: {}\nNumber of slices remaining: {}\n".format(numPizzasNeeded, slicesLeftOver))

  elif numpizzas is not None:
    slicesPerPerson, slicesLeftOver = calcSlices(numppl, numpizzas, numslices)
    print("\nNumber of slices per person: {}\nNumber of slices remaining: {}\n".format(slicesPerPerson, slicesLeftOver))

  else:
    raise Exception("I don't know what to do!")

except Exception as e:
  print("Woops:" , str(e))
