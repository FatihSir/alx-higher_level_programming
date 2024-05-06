#!/usr/bin/python3
""" Create object from a JSON file Module"""


import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file”

    Arguments:
        filename (str): The file where the JSON representation will be loaded
    Return:
        my_obj (obj): The object that will be created from the file
    """
    with open(file=filename, mode='r', encoding='utf-8') as f:
        my_obj = json.load(f)
    return my_obj
