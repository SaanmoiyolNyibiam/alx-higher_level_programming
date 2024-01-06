#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position
    Parameters:
    - my_list: List to be mutated
    - idx: Index of the element to replace
    - element: The value to be used to replace

    Return:
    - If idx is negative, return original list
    - If idx is out of range, return original list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
