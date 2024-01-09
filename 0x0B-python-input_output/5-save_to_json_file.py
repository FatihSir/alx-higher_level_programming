#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file,
        using a JSON representation.
    args:
        my_obj (str): the string that should be written
        filename (txt): the file that will be written into
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
