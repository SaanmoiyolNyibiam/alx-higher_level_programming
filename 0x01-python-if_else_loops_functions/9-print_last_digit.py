#!/usr/bin/python3
""" This is a module that has a function which prints
    the last digit of a number
"""


def print_last_digit(number):
    """ Prints the last digit of a number """

    if number >= 10:
        output = number % 10
        print(output, end="")
    elif number < 0:
        output0 = number * -1
        output = output0 % 10
        print(output, end="")
    else:
        print(number, end="")
        return number
    return output
