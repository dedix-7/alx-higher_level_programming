#!/usr/bin/python3
""" A file fpor the rectanmgle class that inherits from the Base class
"""

import base


class Rectangle(base.Base):
    """A rectangle class that ingherits from the base class
    """


    @width.setter
    def width(self, value):
        """ Setter forthe width attribute
         Args:
              Value; value of the widfth
        """

        if (type(value) is not int):
            raise TypeError('width must be an integer')
        if (value <= 0):
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def width(self):
        """ Property getter for the width attribute
        """

        return (self.__width)

    @height.setter
    def height(self, value):
        """ Setter for the height attribute
        """

        if (type(value) is not int):
            raise TypeError('height must be an integer')
        if (value <= 0):
            raise ValueError('height must be > 0')
        self.__height = value
        return (self.__height)

    @property
    def height(self):
        """ getter for the height attribute
        """

        return (self.__height)

    @x.setter
    def x(self, value):
        """ Setter for the x value coordinate
        """

        if (type(value) is not int):
            raise TypeError('x must be an integer')
        if (value < 0):
            raise ValueError('x must be >= 0')

        self.__x = value
        return (self.__x)

    @property
    def x(self):
        """ getter for the x attribute
        """

        return (self.__x)

    @y.setter
    def y(self, value):
        """setter for the y attrbite
        """

        if (type(value) is not int):
            raise TypeError('y must be an integer')
        if (value < 0):
            raise ValueError('y must be >= 0')
        self.__y = value
        return (self.__y)

    @property
    def y(self):
        """ getter for teh y attribute
        """

        return (self.__y)
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor for the rectangle class
        """

        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        super().__init__(id)

    def area(self):
        """ a method to get the rectangle's area
        """

        return (self.__width * self.__height)

    def display(self):
        """ a method to print out the rectangle using the # char
        """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()
        
    def __str__(self):
        """ A rectangle prinmting string method
        """

        return (f'[Rectangle] {self.id} {self.__x} / {self.__y} - {self.__width} / {self.__height}')

    def update(self, *args, **kwargs):
        """ method to update the attributes
        """

        
        attributes = [self.id, self.__width, self.__height, self.__x, self.__y]
        for i in range(len(args)):
            x = attributes[i]
            x = args[i]
        
