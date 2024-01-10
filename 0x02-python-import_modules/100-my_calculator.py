#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg_c = len(sys.argv)
    arg_v = sys.argv
    if arg_c == 4:
        if arg_v[2] not in ('+', '-', '*', '/'):
            print("{:s}".format("Unknown operator."
                                "Available operators: +, -, * and /"))
            sys.exit(1)
        else:
            a = int(arg_v[1])
            b = int(arg_v[3])
            operator = arg_v[2]
            result = 0
            if operator == '+':
                result = add(a, b)
            elif operator == '-':
                result = sub(a, b)
            elif operator == '*':
                result = mul(a, b)
            elif operator == '/':
                result = div(a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    else:
        print("{:s}".format("Usage: ./100-my_calculator.py"
                            "<a> <operator> <b>"))
        sys.exit(1)
