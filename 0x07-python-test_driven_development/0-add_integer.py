#!/usr/bin/python3
""" A calculation module"""


def add_integer(a, b=98):
    """ A function that returns the sum of two integer variable

    Parameters:
        a (int, float): should be integer or float
        b (int, float): should be integer or float

    Returns:
        int : The sum of the two entered arguments

    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
