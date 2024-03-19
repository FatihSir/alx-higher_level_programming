#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n > length or int(n) < 0:
        return str
    else:
        str = str[:n] + str[n + 1:]
        return str
