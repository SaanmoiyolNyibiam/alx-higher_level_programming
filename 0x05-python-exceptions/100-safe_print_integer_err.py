#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    safe_print_internal_err: Prints an integer
    Parameter:
    value - Value to be divided

    Return:
    True if value has been correctly printed
    Else False
    """
    err_msg = "Exception: Unknown format code 'd' for object of type 'str'"
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("{}".format(err_msg), file=sys.stderr)
        return False
