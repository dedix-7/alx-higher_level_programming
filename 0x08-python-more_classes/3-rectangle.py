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
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be >= 0')
        self.__height = value
        return (self.__height)

    def __init__(self, width=0, height=0):
        """ Constructor for the class
             self: object instance
             width = rectangle width
             height = rectangle height
             initializer
        """

        if (type(width) is not int):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        self.__width = width

        if (type(height) is not int):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """ Gives the area of the rectangle
            self: instance variable
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Givs the  perimeter of the rectangle
        """

        if ((self.__width == 0) or (self.__height == 0)):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Dunder method for printing the object
            @self: instance variable
        """

        pr = []
        for hei in range(self.__height):
            for wid in (self.__width):
                pr.append('#')
            pr.append('\n')
        return (''.join(pr))

    def __repr__(self):
        """ canonical reprsenation
        """

        return (self.__width, self.__height)
