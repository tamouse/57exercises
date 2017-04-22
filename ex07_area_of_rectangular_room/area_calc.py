
SQFT_TO_SQM = 0.09290304

class CalcArgumentError(Exception):
    def __init__(self, arg, msg):
        self.argument = arg
        self.message = msg


def calc(length, width):
    """

    Calculate the area of a room given length and width

    :returns: (area in sq ft, area in sq meters)

    >>> calc(10.0,5.0)
    (50.0, 4.645152)

    >>> calc(2,2)
    (4.0, 0.37161216)

    >>> calc("a", 2)
    Traceback (most recent call last):
        ...
    CalcArgumentError: ('a', 'invalid input: Length must be a number greater than zero')

    >>> calc(2, "a")
    Traceback (most recent call last):
        ...
    CalcArgumentError: ('a', 'invalid input: Width must be a number greater than zero')

    >>> calc(0, 1)
    Traceback (most recent call last):
        ...
    CalcArgumentError: (0.0, 'invalid input: Length must be a number greater than zero')

    >>> calc(1, 0)
    Traceback (most recent call last):
        ...
    CalcArgumentError: (0.0, 'invalid input: Width must be a number greater than zero')

    """

    try:
        length = float(length)
        if not length > 0.0:
            raise ValueError
    except ValueError as err:
        raise CalcArgumentError(length, "invalid input: Length must be a number greater than zero")

    try:
        width = float(width)
        if not width > 0.0:
            raise ValueError
    except ValueError as err:
        raise CalcArgumentError(width, "invalid input: Width must be a number greater than zero")

    area_sqft = length * width
    area_sqm = area_sqft * SQFT_TO_SQM
    return area_sqft, area_sqm

if __name__ == '__main__':
    import doctest
    print("Running Doctests")
    if (doctest.testmod()[0]) == 0:
        print("PASSED!")
