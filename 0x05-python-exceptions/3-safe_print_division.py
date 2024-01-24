#!/usr/bin/python3
def safe_print_division(a, b):
    """
    safe_print_division - Divides two integers and
    prints the result
    Parameters:
    a - First integer to divide
    b - Second integer to divide

    Return:
    The value of the division, otherwise None
    """
    res = 0
    try:
        res = a / b
        print("Inside result: {}".format(res))
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        res = None
    finally:
        return res
