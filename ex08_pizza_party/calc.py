

def calcPizzas(numppl, numslicesper, numslices):
  """
  Given the number of people, the number of slices per person, and the number of slices per pizze,
  return the number of pizzas needed to feed everyone, and the number of pieces left over.

  >>> calcPizzas(8, 1, 8)
  (1, 0)

  >>> calcPizzas(22, 3, 8)
  (8, 2)

  >>> calcPizzas("A", 1, 8)
  Traceback (most recent call last):
      ...
  ValueError: Number of People must be an integer greater than zero

  >>> calcPizzas(8, "a", 8)
  Traceback (most recent call last):
      ...
  ValueError: Number of Slices per Person must be an integer greater than zero

  >>> calcPizzas(8, 1, "a")
  Traceback (most recent call last):
      ...
  ValueError: Number of Slices per Pizza must be an integer greater than zero

  """

  numppl = checkInt(numppl, "Number of People")
  numslicesper = checkInt(numslicesper, "Number of Slices per Person")
  numslices = checkInt(numslices, "Number of Slices per Pizza")

  slicesNeeded = numppl * numslicesper
  pizzasNeeded = slicesNeeded // numslices
  slicesLeftOver = slicesNeeded % numslices
  return pizzasNeeded, slicesLeftOver


def calcSlices(numppl, numpizzas, numslices):
  """
  Given the number of people, pizzas, and slices per pizza, return
  the number of slices each person gets, and the number of leftover
  slices.

  >>> calcSlices(8, 2, 8)
  (2, 0)

  >>> calcSlices(7, 1, 8)
  (1, 1)

  >>> calcSlices("A", 1, 8)
  Traceback (most recent call last):
      ...
  ValueError: Number of People must be an integer greater than zero

  >>> calcSlices(8, "A", 8)
  Traceback (most recent call last):
      ...
  ValueError: Number of Pizzas must be an integer greater than zero


  >>> calcSlices(8, 1, "A")
  Traceback (most recent call last):
      ...
  ValueError: Number of Slices must be an integer greater than zero

  >>> calcSlices(22, 1, 8)
  Traceback (most recent call last):
      ...
  ValueError: Woopss!! Not enough pizzas to feed everyone!!

  """
  numppl = checkInt(numppl, "Number of People")
  numpizzas = checkInt(numpizzas, "Number of Pizzas")
  numslices = checkInt(numslices, "Number of Slices")

  slicesAvailable = numpizzas * numslices

  if numppl > slicesAvailable:
    raise ValueError("Woopss!! Not enough pizzas to feed everyone!!")

  slicesPerPerson = slicesAvailable // numppl
  slicesLeftOver = slicesAvailable % numppl

  return slicesPerPerson, slicesLeftOver

def checkInt(v, desc):
  try:
    x = int(v)
    if x < 1:
      raise ValueError
    return x
  except ValueError as e:
    raise ValueError("{} must be an integer greater than zero".format(desc))

if __name__ == "__main__":
  import doctest
  doctest.testmod()
