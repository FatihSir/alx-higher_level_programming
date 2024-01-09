#!/usr/bin/python3
""" Write to a file module"""


def write_file(filename="", text=""):
    """ A function that writes a string to a text file
    args:
        filename (str): the name of the file to be created or write into
        text (str): the text that will be added to the file
    Returns:
        The number of the written characters
    """
    with open(filename, mode="w", encoding='utf-8') as f:
        return f.write(text)
