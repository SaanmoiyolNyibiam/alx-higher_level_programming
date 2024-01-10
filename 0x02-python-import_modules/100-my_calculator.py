#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg_c = len(sys.argv)
    arg_v = sys.argv
    if arg_c == 4:
        if arg_v[2] not in ('+', '-', '*', '/'):
            print("{:s}".format("Unknown operator. Available operators: +, -, * and /"))
            sys.exit(1)
        else:
            a = int(arg_v[1])
            b = int(arg_v[3])
            operator = arg_v[2]
            if operator == '+':
                print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
            if operator == '-':
                print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
            if operator == '*':
                print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
            if operator == '/':
                print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
    else:
        print("{:s}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)
