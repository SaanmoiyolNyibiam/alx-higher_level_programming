#!/usr/bin/python3
""" This is a module for an I/O function"""
import sys


def read_file(filename=""):
    """
    read_file - This function reads from a file
    parameter:
    - filename: The file to read from
    """
    with open(filename, "r") as input_file:
        file_content = input_file.read()
        print("{}".format(file_content), file=sys.stdout)
