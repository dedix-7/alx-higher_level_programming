#!/usr/bin/python3
""" This module creates the baswe class for the entire project
"""


class Base:
    """ Base class from whch all classes inherit
    """

    __nb_objects = 0
    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
