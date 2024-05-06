#!/usr/bin/python3
""" Save Object to a file Module"""


import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file,
     using a JSON representation:

    Arguments:
        my_obj (str): The string to be saved into a file
                      in a JSON representation.
        filename (str): The file where the JSON representation will be saved
    """
    with open(file=filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
