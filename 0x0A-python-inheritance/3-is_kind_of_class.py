#!/usr/bin/python3
"""Same class or inherit from-Module"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj : The object to be checked.
        a_class : The class to match the type of obj to.
    Returns:
        True: If obj is an instance or inherited instance of a_class
        Otherwise: False.
    """
    if isinstance(obj, a_class):
        return True
    return False
