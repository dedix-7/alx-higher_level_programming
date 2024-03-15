#!/usr/bin/python3
# a module to print a entence in uppercase

def uppercase(str):
    """ A function to print uppercase repr of strings
    """

    for c in str:
        char = ord(c)
        low = ord(c)
        upp = ord(c) - 32
        if low in range(97, 123):
            char = upp
        else:
            char = low
        print("{}".format(chr(char)), end="")
    print("".format())
