#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """A method to initialize a new Student

        Args:
            first_name (str): the first name of the student.
            last_name (str): the last name of the student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A method to get a dictionary of a student"""
        return self.__dict__
