#!/usr/bin/python3
""" This module defines a function that writes to a file"""


def write_file(filename="", text=""):
    """
    write_file - Writes a string to a text file
    and returns the number of characters written
    Parameter:
    - filename: File to write to
    - text: The string to be written to file

    Return:
    The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as input_file:
        n_chars = input_file.write(text)
        return n_chars
