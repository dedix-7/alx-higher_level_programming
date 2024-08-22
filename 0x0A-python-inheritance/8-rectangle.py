#!/usr/bin/python3
""" A module to ineherit from the Base Geometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class to make a simple rectangle
        It inherits from the ase geomrtery for simple uses
    """

    def __init__(self, width, height):
        """ Initialization function
            Args:
                 width - rectangle width
                 height - height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
