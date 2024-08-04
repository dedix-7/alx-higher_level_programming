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

    def set_width(self, value):
        """ Setter forthe width attribute
         Args:
              Value; value of the widfth
        """

        if ((type(value)) is not (int)):
            raise TypeError('width must be an integer')
        if ((value) <= 0):
            raise ValueError('width must be > 0')
        self.__width = value
        return (value)

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

    def setheight(self, value):
        """ Setter for the height attribute
        """

        print('height setter called')
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

        self.__x = value
        return (self.__x)

    def set_x(self, value):
        """ Setter for the x value coordinate
        """

        if (type(value) is not int):
            raise TypeError('x must be an integer') from None
        if (value < 0):
            raise ValueError('x must be >= 0') from None

        self.__x = value
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

    def set_y(self, value):
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

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class
           Args:
              width: width of rectangle
        height: height of rectangle
        x: x -coordinate
        y: y-coordinate
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

        rew = f'[Rectangle] ({self.id}) {self.__x}/{self.__y} '
        tru = f'- {self.__width}/{self.__height}'
        return (rew + tru)

    def update(self, *args, **kwargs):
        """ method to update the attributes
        """

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if kwargs is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ a function to return the dictionary representation of a rectangle
        """

        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x,
                'y': self.__y}
