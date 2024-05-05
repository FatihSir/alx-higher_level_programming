#!/usr/bin/python3
"""Write to a file Module"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8) and
    returns the number of characters written

    Arguments:
        filename (str): the name of the file to be written to
        text (str): the text to be written
    Return:
        num_of_chr (int): the number of characters written
    """
    with open(file=filename, mode='w', encoding='utf-8') as f:
        num_of_chr = f.write(text)
    return num_of_chr
