#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list without modifying the list
    Parameters:
    - my_list: List to be mutated
    - idx: Index at which list will be mutated
    - element: Value to replace with in list

    Return:
    - If idx is negative, return the original list
    - If idx is out of range, return the original list
    """
    if my_list:
        my_list1 = my_list.copy()
        if idx < 0 or idx >= len(my_list):
            return my_list1
        else:
            my_list1[idx] = element
            return my_list1
