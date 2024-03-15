#!/usr/bin/python3
# a moduel to check for lowercase chars

def islower(c):
    """ A function """
    if (ord(c)) in range(97, 123):
        return True
    else:
        return False
