#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 1:
        return my_list[0]
    else:
        max = my_list[0]
        for i in range(len(my_list)):
            if i < len(my_list) - 1:
                if max >= my_list[i + 1]:
                    continue
                else:
                    max = my_list[i + 1]
    return max
