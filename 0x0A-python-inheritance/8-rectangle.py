#!/usr/bin/python3
""" This is a module that defines a class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a class that inherits from BaseGeometry """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, width, width)
        BaseGeometry.integer_validator(self, height, height)
        _Rectangle__height = height
        _Rectangle__width = width
