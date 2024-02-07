#!/usr/bin/python3
""" This module defines a load from json file function """
import json


def load_from_json_file(filename):
    """
    load_from_json_file - Creates an object from a JSON file
    Parameter:
    - filename: The file which object will be created from
    """
    with open(filename) as f:
        json.load(file)
        return data
