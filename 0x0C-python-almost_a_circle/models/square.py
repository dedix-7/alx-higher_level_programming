#!/usr/bin/python3
import rectangle
""" A sqaure class that inherits from rectangle
"""


class Square(rectangle.Rectangle):
    """ A special rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization inheriting from super
        """

        super().__init__(size, id, x, y)
        size = super().__init__(width, height)

    def __str__(self):
        """ override different string methiods
        """

        string = f"[Square] ({self.__id}) {self.__x}/{self.__y} - {self.__size}"
        return (string)

    @property
    def width(self):
        """ getter for the width of the class
        """

        return (super().width())

    @width.setter
    def width(self, value):
        """ A setter for the width of the square
        """

        return (super().width(value))

    @property
    def height(self):
        """ getter for the height of the square
        """

        return (super().height())

    @height.setter
    def height(self, value):
        """ setter for the square height
        """

        return (super().height(value))

    def update(self, *args, **kwargs):
        """ update method for the sqaure
        """

        super().update(*args, **kwargs)
        
