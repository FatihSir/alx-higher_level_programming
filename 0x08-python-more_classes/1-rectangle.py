#!/usr/bin/python3
"""Real definition of a rectangle Module"""


class Rectangle:
    """
    Class that defines properties of rectangle by: (based on 0-rectangle.py).

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of the class Rectangler

        Args:
            width (int): width (by defaults = 0).
            height (int): height (by defaults = 0).
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Property retriver for the width.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width.

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property retriver for the height.

        Returns:
            int: the height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height.

        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
