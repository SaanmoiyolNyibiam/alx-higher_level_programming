#!/usr/bin/python3
import json
""" This module defines a load from json file function """


def load_from_json_file(filename):
    """
    load_from_json_file - Creates an object from a JSON file
    Parameter:
    - filename: The file which object will be created from
    """
    with open(filename, 'r') as f:
        data = json.load(file)
        return data
