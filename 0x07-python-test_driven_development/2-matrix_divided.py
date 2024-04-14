#!/bin/usr/python3
"""A function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix

    Args:
        matrix (list of lists(int, float)): the matrix that it's
        elements should be divided
        div (int, float): the number that the matrix should be divided by

    Return:
        an integer: the addition of a and b
    """
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix(list of lists)"
                        " of integers/floats")
    size = len(matrix[0])
    for row in matrix:
        if not len(row) == size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(item / div, 2) for item in row] for row in matrix]
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt", verbose=True)
