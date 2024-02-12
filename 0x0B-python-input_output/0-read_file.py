#!/usr/bin/python3
""" This is a module for an I/O function"""


def read_file(filename=""):
    """
    read_file - This function reads from a file
    parameter:
    - filename: The file to read from
    """
    with open(filename, encoding="utf-8") as input_file:
        print(input_file.read())
