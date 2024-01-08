#!/usr/bin/python3
"""Only sub class of-Module"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class : The class to match the type of obj to.
    Returns:
        True: If the object is inherited from the specified class.
        Otherwise: False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
