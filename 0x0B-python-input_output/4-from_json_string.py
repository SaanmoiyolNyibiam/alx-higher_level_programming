#!/usr/bin/python3
""" This module defines a string-to-object function """
import json


def from_json_string(my_str):
    """
    from_json_string - Returns the object representation of a json string
    Parameter:
    my_obj: The string to be deserialized

    Return:
    An object(Python data structure)
    """
    return json.loads(my_str)
