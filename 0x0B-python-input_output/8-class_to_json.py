#!/usr/bin/python3
""" Class to JSON """


import json


def class_to_json(obj):
    """
    A function that returns the dictionary description with
    simple data structur (list, dictionary, string, integer
    and boolean) for JSON serialization of an object:

    Arguments:
        obj (obj): is instance of a class

    Return:
        dict_json (dict): the dictionary description of a class
    """
    dict_json = json.dumps(obj.__dict__)
    return dict_json
