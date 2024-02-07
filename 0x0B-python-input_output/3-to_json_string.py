#!/usr/bin/python3
""" This module defines an object to JSON string function """
import json

def to_json_string(my_obj):
    """
    to_json_string - Returns the json representation of an object
    Parameter:
    - my_obj: The obj to be serialized

    Return:
    A string(json represention)
    """
    return json.dumps(my_obj)
