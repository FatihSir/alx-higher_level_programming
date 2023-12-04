#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 1:
        return my_list[0]
    max = my_list[0]
    for value in my_list:
        if max < value:
            max = value
    return max
