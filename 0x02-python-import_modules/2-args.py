#!/usr/bin/python3
import sys

if __name__ = "__main__":
    arg_c = len(sys.argv) - 1
    arg_v = sys.argv

    if arg_c < 2:
        if arg_c == 1:
            print("{:d} argument:".format(arg_c))
            print("{:d}: {:s}".format(1, arg_v[1]))
        else:
            print("{:d} arguments.".format(arg_c))
    if arg_c > 1:
        print("{:d} arguments:".format(arg_c))
        i = 1
        while i <= arg_c:
            print("{:d}: {:s}".format(i, arg_v[i]))
            i += 1
