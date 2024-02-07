#!/usr/bin/python3
"""This module defines a save to json file function"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - Writes an object to a text file, using a JSON representation
    Parameter:
    - my_obj: The obj to be written to file
    - filename: The file which object will be written to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
