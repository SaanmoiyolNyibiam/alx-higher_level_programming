#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets
    Parameters:
    - set_1: First set
    - set_2: Second set

    Return:
    - A set of common elements in two sets
    """
    result_set = set_1.intersection(set_2)
    return result_set
