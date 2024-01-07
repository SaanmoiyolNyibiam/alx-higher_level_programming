#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list
    Parameter:
    - my_list: The list of integers to find in

    Return:
    - If list is empty, return None
    - Else, return the biggest number
    """
    if not my_list:
        return None
    else:
        largest = my_list[0]
        for item in my_list:
            if item > largest:
                largest = item
        return largest
