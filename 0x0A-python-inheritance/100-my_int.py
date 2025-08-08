#!/usr/bin/python3
""" This is a module that defines a class """


class MyInt(int):
    """ This is a class that inherits from int """
    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
