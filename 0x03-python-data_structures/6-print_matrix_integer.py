#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix is None) or (matrix == [[]]):
        print()
        return
    length, width = len(matrix), len(matrix[0])
    for i in range(width):
        for j in range(length):
            if j == length - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=" ")