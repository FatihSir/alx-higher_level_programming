#!/usr/bin/python3
"""A function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """
     A function that prints My name is <first name> <last name> #

    Args:
        first_name (str): The first name - mandatory
        last_name (str): The last name - optional
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt", verbose=True)
