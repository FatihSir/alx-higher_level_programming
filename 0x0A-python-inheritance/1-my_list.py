#!/usr/bin/python3
""" List Module"""


class MyList(list):
    def print_sorted(self):
        """ Public instance method
        Return: prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
