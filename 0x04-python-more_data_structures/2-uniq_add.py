#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list
    Paramters:
    - my_list: The list to add integers from
    Return:
    - The sum result
    """
    my_set = set(my_list)
    print(my_set)
    print(my_list)
    sum = 0
    for item in my_set:
        sum += item
    return sum
