#!/usr/bin/python3
def safe_print_integer(value):
    """
    safe_print_integer - Prints an integer
    value: The integer to be printed

    Return: True if value has been correctly printed
    else, false
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
