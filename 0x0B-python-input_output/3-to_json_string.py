#!/usr/bin/python3
"""To JSON string module"""
import json


def to_json_string(my_obj):
    """ A function that returns the JSON representation of an object (string).
    args:
        my_obj (str): the object that to be converted to JSON
    Returns:
        The JSON representation of an object (string
    """
    return json.dumps(my_obj)
