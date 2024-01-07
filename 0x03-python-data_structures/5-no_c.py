#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all  characters c and C from a string
    Parameters:
    - my_string: The string to remove characters from
    """
    result_string = ""
    for item in my_string:
        if item != 'c' and item != 'C':
            result_string += item
    return result_string
