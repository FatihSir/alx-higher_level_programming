#!/usr/bin/python3
""" This module multiply 2 matrices using numpy module """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ a function that multiplies 2 matrices by using the module NumPy
    Parameters:
        m_a: matrix a
        m_b: matrix b
    Returns:
        returns m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
