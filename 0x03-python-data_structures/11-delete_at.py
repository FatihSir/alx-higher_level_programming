#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx > length - 1 or idx < 0:
        return my_list
    start = my_list[:idx]
    end = my_list[idx + 1:]
    start.extend(end)
    return start
