#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase
    Parameters:
    - str: String to be printed in uppercase
    """
    for char in str:
        output = (
            ord(char) - 32 if 97 <= ord(char) <= 122 else ord(char)
        )
        print("{:c}".format(output), end="")
    print()
