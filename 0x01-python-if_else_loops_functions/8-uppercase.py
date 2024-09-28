#!/usr/bin/python3
""" This is a module that has a string formatting function"""

def uppercase(str):
    """
    Prints a string in uppercase
    Parameters:
    - str: String to be printed in uppercase
    """
    i = 1
    for char in str:
        output = ord(char) - 32 if 97 <= ord(char) <= 122 else ord(char)
        end_val = "\n" if i == len(str) else ""
        print("{:c}".format(output), end=end_val)
        i += 1
