#!/usr/bin/python3
"""A module uses print_square method."""


def print_square(size):
    """Method that prints a square with the character #.

    Parameters:
        size:  the size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
