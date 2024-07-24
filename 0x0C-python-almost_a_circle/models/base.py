#!/usr/bin/python3
""" A base class from where all the others will inherit from
"""


class Base:
    """ The base class for the almost a circle project
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """ The constructor for the class and assigns an id to itself
        """

        if (type(id) is not None):
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
