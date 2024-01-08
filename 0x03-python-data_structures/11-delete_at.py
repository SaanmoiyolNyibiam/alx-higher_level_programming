#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list
    Parameters:
    - my_list: A list of items
    - idx: The index of the item to be deleted

    Return:
    - If idx is negative or out of range, return the original list
    - Else, return a new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
