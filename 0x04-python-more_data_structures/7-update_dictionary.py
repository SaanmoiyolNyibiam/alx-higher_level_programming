#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary
    Parameters:
    - a_dictionary: The dictionary to update
    - key: The key to update
    - value: The value to update

    Return:
    - Updated dictionary
    """
    if type(key) is str:
        a_dictionary[key] = value
    return a_dictionary
