#!/usr/bin/python3
""" Max integer - Unittest """


import unittest
import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class to apply unittest"""
    def setUp(self):
        """A method to set_up the lists to be used in tests"""
        self.list_1 = [2, 4, 5, 10]
        self.list_2 = [-1, -3, 0, -20]
        self.list_3 = ["Mohamed", 10, 2, -2, 2.4]
        self.list_4 = []
        self.list_5 = [-20, -5, -100, -20]
        self.t = (129, 192, 19,)
        self.list_6 = [float('-inf'), float('inf'), 0, 10]
        self.list_7 = [-2.5, 99.99, 25, 0, 32, -90]
        self.list_8 = [1995, 1970, 1985, 1993]

    def test_invalid(self):
        """A method to test invalid values resulted in 'TypeError'"""
        with self.assertRaises(TypeError):
            max_integer(self.list_6)
            max_integer(self.list_3)
            max_integer(6)
            max_integer(8.8)

    def test_infinity(self):
        """A method to test infinity"""
        self.assertEqual(max_integer(self.list_6), float('inf'))

    def test_empty(self):
        """A method to test when None or empty list passed"""
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(self.list_4), None)

    def test_int(self):
        """A method to test regular integer in a list"""
        self.assertEqual(max_integer(self.list_1), 10)
        self.assertEqual(max_integer(self.list_2), 0)
        self.assertEqual(max_integer(self.list_9), 1995)

    def test_negative(self):
        """A method to test regular negative values in a list"""
        self.assertEqual(max_integer(self.list_5), -5)

    def test_float(self):
        """A method to test regular float values in a list"""
        self.assertEqual(max_integer(self.list_7), 99.99)

    def test_one(self):
        """A method to test a single element list"""
        self.assertEqual(max_integer([100]), 100)


if __name__ == "__main__":
    unittest.main(verbosity=True)
