#!/usr/bin/python3
""" This is a module for an I/O function"""
def read_file(filename=""):
    """
    read_file - This function reads from a file
    parameter:
    - filename: The file to read from
    """
    if not filename:
        return
    with open(filename) as input_file:
        file_content = input_file.read()
        print("{:s}".format(file_content))

