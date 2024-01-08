#!/usr/bin/python3
"""Is_same_class Module"""


def is_same_class(obj, a_class):
    """ A function checks if specified object is exactly instance
    Returns:
    True: if the object is exactly an instance
    False: otherwise
    """
    return isinstance(obj, a_class)
