#!/usr/bin/python3
# a script to reimplement python ytecode

def magic_calculation(a, b):
    from magic_calculation_102 import sub, add
    if (a < b):
        c = add(a, b)
        for i in range(4, 6):
            c = add(i, c)
        return (c)
    return (sub(a, b))
