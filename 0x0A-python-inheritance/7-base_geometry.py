#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry():
    """Integer validator"""
    def area(self):
        """Method Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Instance method to validate integers"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
