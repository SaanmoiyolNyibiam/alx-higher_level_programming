#!/usr/bin/python3
"""This module is for my classes"""


class Rectangle:
    """This is a class that defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ returns a string when class is used with the str() function """
        if (self.__height == 0) or (self.__width == 0):
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """ returns a string representation of the object """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ is invoked when the class is about to be destroyed """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle
            Perimeter = 2(width + height)
        """
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return 2 * (self.__width + self.__height)
