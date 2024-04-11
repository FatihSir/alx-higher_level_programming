#!/usr/bin/python3
""" Rectangle Module Definition """


class Rectangle:
    """Rectangle Class Definition with width and height.

    Attributes:
        number_of_instances (int): a class attribute to count
        the created class instances

    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization method to set the height and the width.

        Args:
            width (int): the width of the rectangle (0 by default).
            height (int): the height of the rectangle (0 by default).
         """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """A method to get with attribute value

        Return:
            width (int): returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A method to set rectangle width value.
        Args:
            value (int): the width of the rectangle
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
        return self.__height

    @height.setter
    def height(self, value):
        """A method to set rectangle's height value.

        Args:
            value (int): the height of the rectangle
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
        return area

    def perimeter(self):
        """A method to return rectangle's perimeter.

        Return:
            perimeter (int): returns the rectangle's perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        perimeter = 2 * self.__height + 2 * self.__width
        return perimeter

    def __str__(self):
        """A method that returns the rectangle in '#' symbol string format.

        Return:
            result (str): return the rectangle in '#' symbol string format
        """
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        for i in range(self.__height):
            if i == self.__height - 1:
                result += "#" * self.__width
                return result
            result += "#" * self.__width + "\n"

    def __repr__(self):
        """A method that returns the current rectangle's
        class representation."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """A method to delete an instance of the class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
