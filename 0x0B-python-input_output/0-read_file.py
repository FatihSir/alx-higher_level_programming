#!/usr/bin/python3


def read_file(filename=""):
    """ A function that reads a text file (UTF8) and prints it to stdout
    args:
        filename (str): the name of the file to be read
    Returns:
        prints the content of the file to stdout
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read())
