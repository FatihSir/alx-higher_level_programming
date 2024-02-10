#!/usr/bin/python3
"""Real definition of a rectangle Module"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
    """Create new instance of the class"""
        self.height = height
        self.width = width

    @property
    def width(self):
    """Retrive width value""" 
        return self.__width

    @width.setter
    def width(self, value=0):
    """Set int non negative value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
    """Retrive height value"""
        return self.__height

    @height.setter
    def height(self, value=0):
    """set int non negative value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
