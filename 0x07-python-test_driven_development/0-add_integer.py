#!/usr/bin/python3
"""A function that adds 2 integers"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers and the second number by default is 98

    Args:
        a (int): the first integer to be added
        b (int = 98): the second integer

    Return:
        an integer: the addition of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt", verbose=True)
