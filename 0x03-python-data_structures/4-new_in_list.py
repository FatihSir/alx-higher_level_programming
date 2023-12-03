#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    length = len(my_list) - 1
    for j in range(length + 1):
        new_list.append(my_list[j])
    if idx < 0 or idx > length:
        return new_list
    else:
        new_list[idx] = element
        return new_list
