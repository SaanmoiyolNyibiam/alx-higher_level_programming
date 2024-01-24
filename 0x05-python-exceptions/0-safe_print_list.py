#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    safe_print_list - Prints x elements of a list
    my_list: List to be printed
    x: Number of members of list to print

    Return: The real number of elements printed
    """
    list_len = 0
    i = 0
    index = 0
    for item in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            index += 1
        except IndexError:
            break
    print()
    return index
