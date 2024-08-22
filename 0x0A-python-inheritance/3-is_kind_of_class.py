#!/usr/bin/python3
"""  This module looks to test whether an object is an instance of a class
Or wheher it inherits from it
"""


def is_kind_of_class(obj, a_class):
    """ return true if an object is an instance o the class or inherits a class
        @obj is the object in question
        @class is the class in question
    """

    if (isinstance(obj, a_class) or isinstance(obj, type(a_class))):
        return True
    else:
        return False
