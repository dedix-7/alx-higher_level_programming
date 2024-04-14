#!/usr/bin/python3
# a script to divide
def safe_print_division(a, b):
    # function to divide a and b
    try:
        result = a / b
    except (ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
