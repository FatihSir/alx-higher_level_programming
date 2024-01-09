#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """ A function that appends a string at the end of a text file.
    args:
        filename (str): the name of the file to be created or write into
        text (str): the text that will be added to the file
    Returns:
        The number of the written characters
    """
    with open(filename, mode="a", encoding='utf-8') as f:
        return f.write(text)
