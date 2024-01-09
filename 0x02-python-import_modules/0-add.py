#!/usr/bin/python3
add = __import__("add_0").add

if __name__ == "__main__":
    a = 1
    b = 2
    res = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, res))
