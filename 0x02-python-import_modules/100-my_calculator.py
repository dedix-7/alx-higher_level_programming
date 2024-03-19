#!/usr/bin/python3
# simple calc with command line args

import sys
import calculator_1
if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if (sys.argv[2] not in ['+', '-', '*', '/']):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (sys.argv[2] == '+'):
        op = calculator_1.add
    elif (sys.argv[2] == '-'):
        op = calculator_1.sub
    elif (sys.argv[2] == '*'):
        op = calculator_1.mul
    else:
        op = calculator_1.div
    print(f"{a} {sys.argv[2]} {b} = {op(a, b)}")
