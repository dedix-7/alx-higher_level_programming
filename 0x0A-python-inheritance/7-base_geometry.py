#!/usr/bin/python3
""" Make a class with an area method
    It also uses an integre validator
"""


class BaseGeometry:
    """ Class with an area method
    """

    def area(self):
        """ Method to get the area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ An int validator to ensure the value is fine
        """

        if (type(value) is not int):
            raise TypeError('{} must be an integer'.format(name))
        if (value <= 0):
            raise ValueError('{} must be greater than 0'.format(name))
