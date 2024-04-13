#!/usr/bin/python3
# a script to test int printing

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False
    return True
