#!/usr/bin/python3
""" Module to check an object is an instance of a given class
It also checks that it's an instance of a class that inherits the given
"""


def inherits_from(obj, a_class):
    """ function to check it inherits otherwise it gives fals
    """

    return (isinstance(obj, a_class) and type(obj) is not a_class)
