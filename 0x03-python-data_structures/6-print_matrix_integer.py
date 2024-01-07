#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers
    Paramters:
    - Matrix: The matrix to be printed
    """
    for row in matrix:
        for item in row:
            print("{:d}".format(item), end=" ")
        print()