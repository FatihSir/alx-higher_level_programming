#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """
    A function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:

    Arguments:
        obj (obj): is instance of a class

    Return:
        my_dict (dict): the dictionary description of a class
    """
    my_dict = obj.__dict__
    return my_dict
