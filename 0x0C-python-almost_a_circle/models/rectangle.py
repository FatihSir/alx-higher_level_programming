#!/usr/bin/python3
""" First Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Rectangle's width"""
        return self.__width

    @width.setter
    def width(self, v):
        self.__width = v

    @property
    def height(self):
        """Rectangle's height"""
        return self.__height

    @height.setter
    def height(self, v):
        self.__height = v

    @property
    def x(self):
        """Rectangle's x"""
        return self.__x

    @x.setter
    def x(self, v):
        self.__x = v

    @property
    def y(self):
        """Rectangle's y"""
        return self.__y

    @y.setter
    def y(self, v):
        self.__y = v
