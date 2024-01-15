#!/usr/bin/python3
""" Base class """
from json import dumps, loads
import csv


class Base:
    """ This class will be the “base” of all other classes in this project """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """JSON string to file"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)
