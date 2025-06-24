#!/usr/bin/python3
"""This module is for my classes"""


class Rectangle:
    """This is a class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Type checks the value of the width and assigns it"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Type checks the value of the height and assigns it"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle
            Area = Width * Height
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ returns the perimeter of the rectangle
            Perimeter = 2(width + height)
        """
        if (self.__height or self.__width) == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter
