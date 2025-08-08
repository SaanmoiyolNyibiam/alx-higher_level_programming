#!/usr/bin/python3
""" This is a module that defines a class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """ This is a class that inherits from BaseGeometry """
    def __init__(self, size):
        BaseGeometry.integer_validator(self, size, size)
        self._Square__size = size

    def area(self):
        """ returns the area of the Square """
        return self._Square__size**2

    def __str__(self):
        """ return a string representation of the object """
        return f"[Rectangle] {self._Square__size}/{self._Square__size}"
