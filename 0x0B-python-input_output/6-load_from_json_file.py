#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """A unction that creates an Object from a “JSON file”.
    args:
        filename (txt): the file that will be read from
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())
