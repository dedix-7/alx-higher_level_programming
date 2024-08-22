#!/usr/bin/python3
""" A module that shows inheritance from the Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A square class derived from rectangles
    """

    def __init__(self, size):
        """ Constructor to set the size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Implement previous area
        """

        return (self.__size * self.__size)

    def __str__(self):
        """ Customezie teh string representaion of this
        """

        return ("[Square] {}/{}".format(self.__size, self.__size))
