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

    print_symbol = '#'

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

    number_of_instances = 0

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
        type(self).number_of_instances += 1

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
        if ((self.__width == 0) or (self.__height == 0)):
            return ""
        for hei in range(self.__height):
            for wid in range(self.__width):
                pr.append(self.print_symbol)
            pr.append('\n')
        ret = pr[:-1]
        return (''.join(str(y) for y in ret))

    def __repr__(self):
        """ canonical reprsenation
        """

        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """ method to call when an instance is deleted
        """

        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ a methdo to return the rectangle with a bigger area
              @rect_1: object of the rectangle class
               @rect_2: object of the rectangle class
        Return:
                 the rectangle with bigger area
        """

        if (type(rect_1) is not Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if (type(rect_2) is not Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if (rect_1.area() == rect_2.area()):
            return rect_1
        elif (rect_1.area() > rect_2.area()):
            return rect_1
        else:
            return rect_2
