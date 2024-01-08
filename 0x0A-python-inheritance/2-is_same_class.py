#!/usr/bin/python3
"""Is_same_class Module"""


def is_same_class(obj, a_class):
    """ A function checks if specified object is exactly instance
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True: if the object is exactly an instance
        False: otherwise
    """
    return type(obj) == a_class
