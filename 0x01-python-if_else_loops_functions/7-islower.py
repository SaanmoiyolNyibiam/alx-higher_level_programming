#!/usr/bin/python3
def islower(c):
    """
    Checks for a lowercase character
    Parameter:
    - c: The character to be checked if it lowercase

    Return:
    - True if c is lowercase, else False
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
