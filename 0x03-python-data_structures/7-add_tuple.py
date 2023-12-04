#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a, length_b = len(tuple_a), len(tuple_b)
    if length_a == 1:
        tuple_a = tuple_a[0], 0
    elif length_a == 0:
        tuple_a = 0, 0
    elif length_a > 2:
        tuple_a = tuple_a[:2]
    elif length_b == 1:
        tuple_b = tuple_b[0], 0
    elif length_b == 0:
        tuple_b = 0, 0
    elif length_b > 2:
        tuple_b = tuple_b[:2]
    tuple_c = tuple(x + y for x, y in zip(tuple_a, tuple_b))

    return tuple_c
