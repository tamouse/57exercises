
SQFT_TO_SQM = 0.09290304

class ArgumentError(Exception):
    def __init__(self, argument, message):
        self.argument = argument
        self.message = message

def calc(length, width):
    """

    Calculate the area of a room given length and width

    :returns: (area in sq ft, area in sq meters)

    >>> calc(10.0,5.0)
    (50.0, 4.645152)

    >>> calc(10, 5.0)
    Traceback (most recent call last):
        ...
    ArgumentError: (10, 'Length must be a float')

    >>> calc(10.0, 5)
    Traceback (most recent call last):
        ...
    ArgumentError: (5, 'Width must be a float')
    """

    if not isinstance(length, float):
        raise ArgumentError(length, "Length must be a float")
    if not isinstance(width, float):
        raise ArgumentError(width, "Width must be a float")

    area_sqft = length * width
    area_sqm = area_sqft * SQFT_TO_SQM
    return area_sqft, area_sqm

if __name__ == '__main__':
    import doctest
    doctest.testmod()
