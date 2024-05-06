#!/usr/bin/python3
""" To JSON string Module"""

import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object (string)

    Arguments:
        my_obj (obj): The object to be converted to JSON representation.
    Return:
        json_repr (json): the json representation of the object
    """
    json_repr = json.dumps(my_obj)
    return json_repr
