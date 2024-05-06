#!/usr/bin/python3
"""  Student to JSON with filter"""


class Student:
    """ a class Student that defines a student

    Attributes:
        first_name : Student's first name
        last_name : Student's last name
        age : Student's age
    """
    first_name = ""
    last_name = ""
    age = None

    def __init__(self, first_name, last_name, age):
        """A method that initiate the instance of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A method retrieves a dictionary representation of a Student instance
            - If attrs is a list of strings, only attribute names
              contained in this list must be retrieved.
            - Otherwise, all attributes must be retrieved
        """
        filtered_dict = {}
        if attrs is None:
            filtered_dict = self.__dict__
        else:
            for key in attrs:
                if key in self.__dict__.keys():
                    filtered_dict[key] = self.__dict__[key]
        return filtered_dict
