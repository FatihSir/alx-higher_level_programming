#!/usr/bin/python3
"""Append to a file Module"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added

    Arguments:
        filename (str): the name of the file to be appended to
        text (str): the text to be appended
    Return:
        num_of_chr (int): the number of characters added
    """
    with open(file=filename, mode='a', encoding='utf-8') as f:
        num_of_chr = f.write(text)
    return num_of_chr
