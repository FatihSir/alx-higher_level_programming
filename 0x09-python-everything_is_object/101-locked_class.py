#!/usr/bin/python3
""" Defining a class LockedClass """


class LockedClass:
    """
    The class prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.

    Attribuites:
    first_name (str): the first name of the user
    """

    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = "first_name"
