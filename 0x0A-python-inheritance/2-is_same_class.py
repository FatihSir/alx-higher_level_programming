#!/usr/bin/python3
"""Is_same_class Module"""


def is_same_class(obj, a_class):
    """ A function checks if specified object is exactly instance
    Return : returns True if the object is exactly an instance
    of the specified class ; otherwise False
    """
    return isinstance(obj, a_class)
