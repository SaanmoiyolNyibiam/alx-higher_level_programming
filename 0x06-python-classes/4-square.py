#!/usr/bin/python3
""" This module defines a class that defines a square """


class Square:
    """ This class defines a square """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ Returns the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of the square """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of the square """
        return self.__size ** 2
