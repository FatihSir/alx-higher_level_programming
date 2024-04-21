#!/usr/bin/python3
""" Matrix multiplication - Unittest """


import unittest
import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
matrix_mul = __import__('100-matrix_mul').matrix_mul

class TestMaxInteger(unittest.TestCase):
    """A class to apply unittest"""
    def setUp(self):
        """A method to set_up the lists to be used in tests"""
        self.a_1 = [[]]
        self.b_1 = [[]]

        self.a_2 = [
            [3, 4, 5],
            [3, 5, 6]
        ]

        self.b_2 = [
            [4, 4, 3],
            [6, 9, 6]
        ]

        self.a_3 = 3
        self.b_3 = 19

        self.a_4 = [3, 5, 6]
        self.b_4 = [4, 6, 2]

        self.a_5 = [
            ["M", 3.5],
            [5.9, 7.9]
        ]
        self.b_5 = [
            [5, 7.6],
            ["A", 6]
        ]

        self.a_6 = [
            [4, 3, 5],
            [4, 9],
            [1, 9, 0]
        ]
        self.b_6 = [
            [7, 2, 1],
            [6, 1.1, 0],
            [2, 8]
        ]
        self.a_7 = None
        self.b_7 = None

        self.a_8 = [
            [4, 2, 5],
            [4, 0, -1],
            [9, 10, -5]
        ]
        self.b_8 = [
            [5, 2, 0.1],
            [5, -1, 2],
            [2, 1, 6]
        ]

        self.a_9 = [
            [float('inf'), 3],
            [3, 5]
        ]
        self.b_9 = [
            [4, 2],
            [3, 6]
        ]

    def test_invalid(self):
        with self.assertRaises(ValueError):
            # Empty matrices
            matrix_mul(self.a_1, self.b_1)
            # Not compatible
            matrix_mul(self.a_2, self.b_2)
            # None
            matrix_mul(self.a_7, self.b_2)
            matrix_mul(self.a_2, self.b_7)

    def test_type(self):
        with self.assertRaises(TypeError):
            # Not a list
            matrix_mul(self.a_3, self.b_2)
            matrix_mul(self.a_2, self.b_3)
            # Not a list of lists
            matrix_mul(self.a_4, self.b_2)
            matrix_mul(self.a_2, self.b_4)
            # Neither an integer nor float
            matrix_mul(self.a_5, self.b_2)
            matrix_mul(self.a_2, self.b_5)
            # Not a rectangle
            matrix_mul(self.a_6, self.b_2)
            matrix_mul(self.a_2, self.b_6)

    def test_regular(self):
        result = [
            [40, 11, 34.4],
            [18, 7, -5.6],
            [85, 3, -9.100000000000001]
        ]
        self.assertEqual(matrix_mul(self.a_8, self.b_8), result)

    def test_inf(self):
        # Test inf
        result = [
            [float('inf'), float('inf')],
            [27, 36]
        ]
        self.assertEquals(matrix_mul(self.a_9, self.b_9), result)


if __name__ == "__main__":
    unittest.main(verbosity=True)
