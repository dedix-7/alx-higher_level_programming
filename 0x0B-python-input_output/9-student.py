#!/usr/bin/python3
""" A module to make a class that returns dict repre of its instance
"""


class Student:
    """ Class to generate objects
    """

    def __init__(self, first_name, last_name, age):
        """ Constructor arguments
        """

        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """ retrives dict repre of studnte object
        """

        if (type(attrs) is list):
            return (dict(attrs))
        else:
            return (self.__dict__)
