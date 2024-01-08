#!/usr/bin/python3
""" My integer module"""


class MyInt(int):
    """ My integer class"""
    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
