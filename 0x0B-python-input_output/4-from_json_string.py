#!/usr/bin/python3
""" From JSON string to Object Module"""

import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)
    represented by a JSON string

    Arguments:
        my_str (json): The JSON string to be converted to
                        string representation.
    Return:
        str_repr (str): the string representation of the JSON string
    """
    str_repr = json.loads(my_str)
    return str_repr
