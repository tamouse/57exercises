

def calc(numppl, numpizzas, numslices):
  """
  Given the number of people, pizzas, and slices per pizza, return
  the number of slices each person gets, and the number of leftover
  slices.

  >>> calc(8, 2, 8)
  (2, 0)

  >>> calc(7, 1, 8)
  (1, 1)

  >>> calc("A", 1, 8)
  Traceback (most recent call last):
      ...
  ValueError: Number of People must be an integer greater than zero

  >>> calc(8, "A", 8)
  Traceback (most recent call last):
      ...
  ValueError: Number of Pizzas must be an integer greater than zero


  >>> calc(8, 1, "A")
  Traceback (most recent call last):
      ...
  ValueError: Number of Slices must be an integer greater than zero

  >>> calc(22, 1, 8)
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
