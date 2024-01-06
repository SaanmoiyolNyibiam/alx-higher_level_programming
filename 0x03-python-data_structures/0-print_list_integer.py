#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints each element of a list as an integer

    Parameters:
    - my_list (list): A list that contains integers
    """
    for item in my_list:
        print("{:d}".format(item))
