#!/usr/bin/python3
""" A file for the rectanmgle class that inherits from the Base class
"""

from models import base


class Rectangle(base.Base):
    """A rectangle class that ingherits from the base class
    """

    @property
    def width(self):
        """ Property getter for the width attribute
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter forthe width attribute
         Args:
              Value; value of the widfth
        """

        if ((type(value)) is not (int)):
            raise TypeError('width must be an integer')
        if ((value) <= 0):
            raise ValueError('width must be > 0')
        self.__width = value
        return (self.__width)

    @property
    def height(self):
        """ getter for the height attribute
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter for the height attribute
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if (value <= 0):
            raise ValueError('height must be > 0')
        self.__height = value
        return (self.__height)

    @property
    def x(self):
        """ getter for the x attribute
        """

        return (self.__x)

    @x.setter
    def x(self, value):
        """ Setter for the x value coordinate
        """

        if (type(value) is not int):
            raise TypeError('x must be an integer') from None
        if (value < 0):
            raise ValueError('x must be >= 0') from None

        self.x = value
        return (self.__x)

    @property
    def y(self):
        """ getter for the y variable and value
        """

        return (self.__y)

    @y.setter
    def y(self, value):
        """ Setter for the y variable

        Args:
            value - value to set y variable to
        """

        if (type(value) is not int):
            raise TypeError('y must be an integer')
        if (value < 0):
            raise ValueError('y must be >= 0')
        self.__y = value
        return (self.__y)

#    width = property(fget=width_get, fset=width_set)
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor for the rectangle class
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

        rew = f'[Rectangle] {self.id} {self.__x} / {self.__y}'
        tru = f'- {self.__width} / {self.__height}'
        return (rew + tru)

    def update(self, *args, **kwargs):
        """ method to update the attributes
        """

        attributes = [self.id, self.__width, self.__height, self.__x, self.__y]
        guesses = [id, width, height, x, y]
        for i in range(len(args)):
            x = attributes[i]
            x = args[i]
        if ((len(args) <= 0)):
            if ((len(kwargs) <= 0)):
                pass
            else:
                for key, value in kwargs:
                    if (key in guesses):
                        setattr(self, key, value)

    def to_dictionary(self):
        """ a function to return the dictionary representation of a rectangle
        """

        return {'id': self.__id, 'width': self.__width,
                'height': self.__height, 'x': self.__x,
                'y': self.__y}
