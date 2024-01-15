#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ quare class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square Information"""
        return '[{}] ({}) {}/{} - {}'.format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """square's size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """__Update Method"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates Method"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Dictionary Representation Method"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
