#!/usr/bin/python3

def lookup(obj):
    """
    lookup - Returns the list of available attributes
    and methods of an object
    Parameter:
    - obj: Object to prints its methods and attributes

    Return:
    A list of attributes and methods
    """
    lookup_res = obj.__dict__
    return lookup_res
