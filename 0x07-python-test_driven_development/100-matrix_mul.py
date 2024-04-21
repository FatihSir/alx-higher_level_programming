#!/usr/bin/python3
"""A function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices and return the result

    Args:
        m_a (list of lists): the first matrix
        m_b (list of lists): the second matrix

    Return:
        result (list of lists): the multiplication
        of the first and the second matrix
    """
    size_a = None
    size_b = None
    rows_a = 0
    rows_b = 0

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        rows_a += 1
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if size_a is None:
            size_a = len(row)
        if not len(row) == size_a:
            raise TypeError("each row of m_a must be of the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise ValueError("m_a should contain only integers or floats")
    for row in m_b:
        rows_b += 1
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if size_b is None:
            size_b = len(row)
        if not len(row) == size_b:
            raise TypeError("each row of m_b must be of the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise ValueError("m_b should contain only integers or floats")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not size_a == rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(size_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(size_b):
            for k in range(size_a):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt", verbose=True)
