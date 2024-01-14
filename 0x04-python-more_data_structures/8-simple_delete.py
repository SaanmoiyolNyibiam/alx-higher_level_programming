#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary
    Parameters:
    - a_dictionary: The dictonary to delete a key in
    - key: The key to be deleted

    Return: The edited dictionary
    """
    if type(key) is str:
        if key in a_dictionary.keys():
            del a_dictionary[key]
    return a_dictionary
