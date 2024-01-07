#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Finds the multiples of 2 in a list
    Parameters:
    - my_list: The list to be evaluated

    Return:
    - A new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
    """
    my_list1 = []
    for item in my_list:
        res = item % 2
        if res == 0:
            my_list1.append(True)
        else:
            my_list1.append(False)
    return my_list1
