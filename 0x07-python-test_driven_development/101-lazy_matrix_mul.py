#!/usr/bin/python3
"""Lazy matrix multiplication"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices by using the module NumPy

    Args:
        m_a (list of lists): the first matrix
        m_b (list of lists): the second matrix

    Return:
        result (list of lists): the multiplication of
        the first and the second matrix
    """

    result = np.matmul(m_a, m_b)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt", verbose=True)
