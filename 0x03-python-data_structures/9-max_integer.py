#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max = my_list[0]
    for value in my_list:
        if max < value:
            max = value
    return max
