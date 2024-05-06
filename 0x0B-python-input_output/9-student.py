#!/usr/bin/python3
""" Student to JSON """


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

    def to_json(self):
        """A method retrieves a dictionary
        representation of a Student instance"""

        return self.__dict__
