#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds 2 tuples
    Parameters:
    -tuple_a: First tuple to be added
    -tuple_b: Second tuple to be added

    Return: A tuple with two integers
    """
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res
