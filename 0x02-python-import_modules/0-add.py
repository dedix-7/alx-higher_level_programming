#!/usr/bin/python3
# import from a local module

if __name = "__main__":
    from add_0 import add
    a, b = 1, 2
    print("{} + {} = {}".format(a, b, add(a, b)))
