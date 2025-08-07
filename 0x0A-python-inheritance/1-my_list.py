#!/usr/bin/python3
""" This is a module that defines a class """

class MyList(list):
    """ This is a class that inherits from list """
    def print_sorted(self):
        """ Prints a list, but sorted(ascending order) """
        print(sorted(self))
