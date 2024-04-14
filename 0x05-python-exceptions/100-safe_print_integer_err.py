#!/usr/bin/python3
import sys
# print an int and errs to stderr


def safe_print_integer_err(value):
    # funtion to print the int
    try:
        print("{:d}".format(value))
    except Exception as mess:
        print("Exception: {}".format(mess), file=sys.stderr)
        return (False)
    return (True)
