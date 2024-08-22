#!/usr/bin/python3
""" A module to make a class that returns dict repre of its instance
    document the module for checker
"""


class Student:
    """ Class to generate objects
    """

    def __init__(self, first_name, last_name, age):
        """ Constructor arguments and function
            Args:
                 first_name(str): non-optional
        """

        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """ retrives dict representation of student object
              retrive them using json
        """

        if (type(attrs) is list and all(type(el) is str for el in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return (self.__dict__)
