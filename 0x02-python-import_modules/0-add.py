#!/usr/bin/python3
# import from a local module

from add_0 import add
if __name__ == "__main__":
    a, b = 1, 2
    print("{} + {} = {}".format(a, b, add(a, b)))
