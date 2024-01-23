#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    safe_print_list - Prints x elements of a list
    my_list: List to be printed
    x: Number of members of list to print

    Return: The real number of elements printed
    """
    try:
        list_len = 0
        i = 0
        index = 1
        for item in my_list:
            list_len += 1

        while i < x:
            if index == list_len or index == x:
                print("{}".format(my_list[i]), end="\n")
                break
            else:
                print("{}".format(my_list[i]), end="")
            index += 1
            i += 1
        return index
    except:
        print("{:s}".format("An error occured"))