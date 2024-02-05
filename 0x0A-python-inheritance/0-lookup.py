#!/usr/bin/python3
""" My lookup module """
def lookup(obj):
    """
    lookup - Returns the list of available attributes
    and methods of an object
    Parameter:
    - obj: Object to prints its methods and attributes

    Return:
    A list of attributes and methods
    """
    lookup_res = dir(obj)
    return lookup_res
