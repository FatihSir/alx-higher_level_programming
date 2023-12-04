#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    rows, columns = len(matrix), len(matrix[0])
    for row in matrix:
        for value in row:
            if row.index(value) != rows - 1:
                print("{:d}".format(value), end=" ")
            else:
                print("{:d}".format(value), end="")
        print()
