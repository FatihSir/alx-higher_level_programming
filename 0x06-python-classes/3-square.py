#!/usr/bin/python3
""" Square module """


class Square:
    """
    class Square has a private instance attribute
    """
    def __init__(self, size=0):
        """
        Params:
            size: The size of the square

        Raise:
            TypeError: if the argument size is not an integer
            ValueError: if the argument size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
    def area: Public instance method
    area(self): that returns the current square area
    """
    def area(self):
        return self.__size**2
