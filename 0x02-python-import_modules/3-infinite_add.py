#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_v = sys.argv
    arg_c = len(sys.argv) - 1
    if arg_c < 1:
        print("{:d}".format(0))
    else:
        i = 1
        res = 0
        while i <= arg_c:
            res += int(arg_v[i])
            i += 1
        print("{:d}".format(res))
