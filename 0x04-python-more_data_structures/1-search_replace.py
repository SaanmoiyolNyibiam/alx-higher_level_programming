#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element by another in a new list
    Parameters:
    - my_list: Initial list
    - search: The element to replace in the list
    - replace: The new element
    """
    my_list_cp = my_list.copy()
    for index, item in enumerate(my_list_cp):
        if search == item:
            my_list_cp[index] = replace
    return my_list_cp
