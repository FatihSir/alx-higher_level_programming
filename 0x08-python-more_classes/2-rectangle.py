#!/usr/bin/python3
""" Rectangle Module Definition """


class Rectangle():
    """Rectangle Class Definition with width and height.

    Attributes:
        width (int): the width of the rectangle (private).
        height (int): the height of the rectangle (private).
    """

    def __init__(self, width=0, height=0):
        """Initialization method to set the height and the width.

        Args:
            width (int): the width of the rectangle (0 by default).
            height (int): the height of the rectangle (0 by default).
         """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """A method to get with attribute value

        Return:
            width (int): returns the width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """A method to set rectangle width value.
        Args:
            width (int): the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A method to return the rectangle's height value

        Return:
            height (int): returns the rectangle's height value
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """A method to set rectangle's height value.

        Args:
            height (int): the height of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """A method that returns rectangle's area.

        Return:
            area (int): returns the rectangle's area.
        """
        area = self.__height * self.__width
        return (area)

    def perimeter(self):
        """A method to return rectangle's perimeter.

        Return:
            perimeter (int): returns the rectangle's perimeter
        """

        perimeter = 2 * self.__height + 2 * self.__width
        return (perimeter)
