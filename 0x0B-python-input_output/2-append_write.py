#!/usr/bin/python3
""" This module defines a function that appends to a file"""


def append_write(filename="", text=""):
    """
    append_write - Appends a string to the end of a text file
    and returns the number of characters appended
    Parameter:
    - filename: File to append to
    - text: The string to be append to file

    Return:
    The number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as input_file:
        n_chars = input_file.write(text)
        return n_chars
