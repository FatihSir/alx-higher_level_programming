#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ".", "?" and ":"
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines
    after each of these characters: ".", "?" and ":"

    Args:
        text (str): The text to be processed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for i in text:
        if flag == 1:
            if i == " ":
                continue
            else:
                flag = 0
        print(i, end="")
        if i in [".", "?", ":"]:
            print()
            print()
            flag = 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt", verbose=True)
