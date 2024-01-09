#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """ A function that returns an object (Python data structure)
        represented by a JSON string.
    args:
        my_str (str): the json string that to be converted to object
    Returns:
        The object string representation of a json string
    """
    return json.loads(my_str)
