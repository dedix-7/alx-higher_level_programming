#!/usr/bin/python3
""" A script looking to disassemblr the python bytecode
"""
from math import pi


class MagicClass:
    """ The reassembled class
    """

    def __init__(self, radius=0):
        """ constructor for the class
        """

        if (type(radius) not in [float, int]):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ area of the circle

        """

        return ((math.pi) * (self.__radius ** 2))

    def circumference(self):
        """ method to give the circmference
        """

        return (2 * pi * self.__radius)
