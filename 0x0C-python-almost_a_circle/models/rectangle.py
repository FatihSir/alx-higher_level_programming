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
        self.validate_integer("width", v)
        self.__width = v

    @property
    def height(self):
        """Rectangle's height"""
        return self.__height

    @height.setter
    def height(self, v):
        self.validate_integer("height", v)
        self.__height = v

    @property
    def x(self):
        """Rectangle's x"""
        return self.__x

    @x.setter
    def x(self, v):
        self.validate_integer("x", v, False)
        self.__x = v

    @property
    def y(self):
        """Rectangle's y"""
        return self.__y

    @y.setter
    def y(self, v):
        self.validate_integer("y", v, False)
        self.__y = v

    def validate_integer(self, name, v, distinct=True):
        """ Validate attributes method """
        if type(v) != int:
            raise TypeError("{} must be an integer".format(name))
        if distinct and v <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif not distinct and v < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """ Area calculator method"""
        return self.__width * self.__height

    def display(self):
        """ Rectangle Displaying Method """
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def __str__(self):
        """ Class Info Method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update Method

        Args:
            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """
        if args is not None and len(args) is not 0:
            l_attribute = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, l_attribute[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary Representation of this class"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
