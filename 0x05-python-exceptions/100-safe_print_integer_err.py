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
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
