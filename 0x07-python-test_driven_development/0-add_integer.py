#!/usr/bin/python3
""" A module to define an add function

The function defines a function to add integers and floats
"""


def add_integer(a, b=98):
    """ A function to add two numbers
        args:
             a - fiurst number
             b - second number
        Return:
                The sum of the numbers
     raides an error or exception when another type is passed
    """

    if (type(a) not in [int, float]):
        raise TypeError('a must be an integer')
    if (type(b) not in [int, float]):
        raise TypeError('b must be an integer')
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return (a + b)
