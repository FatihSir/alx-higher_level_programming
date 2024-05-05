#!/usr/bin/python3
"""Read file Module"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout

    Arguments:
        filename (str): the name of the file to be read
    """
    with open(file=filename, mode='r', encoding='utf-8') as f:
        text = f.read()
        print(text, end="")
