#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys
    Parameters:
    - a_dictonary: The dictionary to be sorted
    """
    sorted_keys = sorted(a_dictionary)
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
