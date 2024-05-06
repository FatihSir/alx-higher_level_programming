#!/usr/bin/python3
""" Load, add, save Module
A script that adds all arguments to a Python list,
and then save them to a file:
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    my_list = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    my_list = []

if len(argv) < 2:
    print("Nothing here")
else:
    for i in range(len(argv)):
        if i == 0:
            continue
        my_list.append(argv[i])

save_to_json_file(my_list, filename='add_item.json')
my_obj = load_from_json_file(filename='add_item.json')
