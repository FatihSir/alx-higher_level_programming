#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for item in my_list:
        list.append(item % 2 == 0)
    return list
