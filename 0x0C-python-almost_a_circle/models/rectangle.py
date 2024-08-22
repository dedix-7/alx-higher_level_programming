#!/usr/bin/python3
import base
""" A module to create the rectangle class
"""


class Rectangle(base.Base):
    """ A class that inherots from the base and makes a rectangle
    """

    @property
    def width(self):
        """ getter for the wisth class
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """ A setter for the width value
        """

        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value
        return (self.__width)

    @property
    def height(self):
        """ A getter for the height property of te class
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """ A setter for the height property
        """

        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value
        return (self.width)

    @property
    def x(self):
        """ Getter for the x value"""

        return (self.__x)

    @x.setter
    def x(self, value):
        """ Setter for the x value
        """

        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value
        return (self.__x)

    @property
    def y(self):
        """ A getter for the y attribute
        """

        return (self.__y)

    @y.setter
    def y(self, value):
        """ A setter for the y attribute
        """

        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
        return (self.__y)

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor for the Rectangle class
            Args:
                  width: private isntance attribute, width of rectangle
                  height: height of the rectangle
                  x: private isntance attribute showing x point
                  y: point on rectangle
                  id of the rectangle object
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def area(self):
        """ Gets the area of the rectangle
        """

        return (self.__width * self.__height)

    def display(self):
        """ Display the rectangle using hash
        """

        for r in (range(self.__y)):
            print()
        for h in range(self.__height):
            for w in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print(f"#", end="")
            print()

    def __str__(self):
        """ Override the stsr nmethod for this class
        """

        part1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        part2 = f" - {self.__width} - {self.__height}"
        return (part1 + part2)

    def update(self, *args, **kwargs):
        """ A method to update the argunmenst given by init
        """

        if (args is not None and args[0] is not None):
            self.__id = kwargs.get('id', self.__id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__height)
            self.__y = kwargs.get('y', self.__y)
        else:
            self.__id = args[0]
            self.__width = self.width(args[1])
            self.__height = self.width(args[2])
            self.__x = self.x(args[3])
            self.__y = self.y(args[4])
