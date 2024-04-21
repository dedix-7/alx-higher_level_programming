#!/usr/bin/python3
""" This project os to defne a simple sqaure class
"""


class Square:
    """ The definition fr the quare class
    """

    def __init__(self, size=0):
        """ Instantiating the size of the class
        """

        self.__size = size

        @property
    def __size(self):
        """ Getter for the size attribute
        """

        return (self.__size)

    @__size.setter
    def __size(self, value):
        """ setter for the size attribute
        """

        if ((type(value)) is not int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value
        return (self.__size)

