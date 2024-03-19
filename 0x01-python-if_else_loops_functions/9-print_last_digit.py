#!/usr/bin/python3
def print_last_digit(number):
    if type(number) == str:
        return "Traceback (most recent call last):"
    number = str(number)
    last_digit = number[-1:]
    print("{}".format(last_digit), end="")
    return last_digit
