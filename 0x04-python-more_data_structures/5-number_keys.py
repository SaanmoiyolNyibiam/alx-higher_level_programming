#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary
    Parameters:
    - a_dictionary: The dictionary to check
    the number of keys it has

    Return:
    - The number of keys in the dictionary
    """
    dict_len = 0
    for item in a_dictionary:
        dict_len += 1
    return dict_len
