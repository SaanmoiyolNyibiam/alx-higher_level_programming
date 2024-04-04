#!/usr/bin/python3
""" This module defines a class that defines a square """


class Square:
    """ This class defines a square """
    def __init__(self, size=0):
        self.size = size
        # if isinstance(size, int) is False:
        #     raise TypeError("size must be an integer")
        # if size < 0:
        #     raise ValueError("size must be >= 0")
        # self.__size = size

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

    def my_print(self):
        """ Prints the square with the character '#' """
        if self.__size == 0:
            print()
        else:
            line = 1
            size = self.__size
            while (line <= size):
                column = 1
                while (column <= size):
                    if column == size:
                        print("{}".format("#"))
                    else:
                        print("{}".format("#"), end="")
                    column += 1
                line += 1
