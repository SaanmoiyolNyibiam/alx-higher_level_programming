#!/usr/bin/python3
""" This is a module that defines a class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a class that inherits from BaseGeometry """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, width, width)
        BaseGeometry.integer_validator(self, height, height)
        self._Rectangle__height = height
        self._Rectangle__width = width

    def area(self):
        """ returns the area of the rectangle """
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """ returns the a string representation of the object """
        return f"[Rectangle] {self._Rectangle__width}/{self._Rectangle__height}"
