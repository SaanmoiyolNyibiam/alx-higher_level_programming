#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieves an element from a list
    Parameters:
    - my_list: A list of items
    - idx: The index of the items to be retrieved

    Return:
    - If idx is negative, none
    - If idx is out of range, none
    """
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
