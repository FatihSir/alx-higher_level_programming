#!/usr/bin/python3
""" Rectangle Module Definition """


class Rectangle:
    """Rectangle Class Definition with width and height.

    Attributes:
        number_of_instances (int): a class attribute to count
        the created class instances

        print_symbol (any): a symbol uses to print the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization method to set the height and the width.

        Args:
            width (int): the width of the rectangle (0 by default).
            height (int): the height of the rectangle (0 by default).
         """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
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
            for j in range(self.__width):
                result = result + f"{self.print_symbol}"
                if i == self.__height - 1 and j == self.__width - 1:
                    return result
            result = result + "\n"
        return result

    def __repr__(self):
        """A method that returns the current rectangle's
        class representation."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """A method to delete an instance of the class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A static method to compare between two rectangles' areas

        Args:
            rect_1 (Rectangle Instance): the first rectangle
            rect_2 (Rectangle Instance): the second rectangle

        Return:
            return the bigger rectangle and if they are equal return rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """A class method that returns a new Rectangle instance
        with width == height == size

        Args:
            size (int): the size of the square
        Return:
            returns a new rectangle instance
        """
        return Rectangle(size, size)
