#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    new_set = set(my_list)
    result = sum(new_set)
    return result
