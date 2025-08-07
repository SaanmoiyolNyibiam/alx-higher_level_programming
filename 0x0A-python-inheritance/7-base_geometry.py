#!/usr/bin/python3
""" This is a module that defines a class """


class BaseGeometry():
    """ This is a python class """
    def area(self):
        """
        This is function that
        raises an Exception with the
        message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This is a function that validates value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
