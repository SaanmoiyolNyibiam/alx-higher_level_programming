#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds 2 tuples
    Parameters:
    -tuple_a: First tuple to be added
    -tuple_b: Second tuple to be added

    Return: A tuple with two integers
    """
    len_ta = len(tuple_a)
    len_tb = len(tuple_b)
    if len_ta < 2:
        i = 0
        while i < 2:
            tuple_a += (0,)
            i += 1
    if len_tb < 2:
        i = 0
        while i < 2:
            tuple_b += (0,)
            i += 1
    if len_ta >= 2 or len_tb >= 2:
        arg1 = tuple_a[0] + tuple_b[0]
        arg2 = tuple_a[1] + tuple_b[1]
        res = (arg1,) + (arg2,)
    return res
