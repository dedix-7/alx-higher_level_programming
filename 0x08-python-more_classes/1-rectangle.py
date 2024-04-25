#!/usr/bin/python3
""" A moduel to make a rectangle class
"""


class Rectangle:
    """ The actual class definition
    """

    @property
    def width(self):
        """ Getter for the width property
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter for the width attribute

        Args:
             @value: value to set the width to
        """

        if (type(value) is not int):
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be >= 0')
        self.__width = value
        return (self.__width)

    @property
    def height(self):
        """ Getter for the height attribute
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter for the height attribute

            Args:
                 value:
                       the value toset theheight to
        """

        if (type(value) is not int):
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be >= 0')
        self.__height = value
        return (self.__height)

    def __init__(self, width=0, height=0):
        """ Constructor for the class
             self: object instance
             width = rectangle width
             height = rectangle height
             initializer
        """

        self.__width = width
        self.__height = height
