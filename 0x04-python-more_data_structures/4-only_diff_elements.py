#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set
    Parameters:
    - set_1: The first set
    - set_2: The second set

    Return:
    - A set of all elements present in only one set
    """
    result_set = set_1.symmetric_difference(set_2)
    return result_set
