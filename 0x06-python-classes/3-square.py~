#!/usr/bin/python3
""" This project os to defne a simple sqaure class
"""


class Square:
    """ The definition fr the quare class
    """

    def __init__(self, size=0):
        """ Instantiating the size of the class
        """

        if ((type(size)) is not int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """ Getter for the size attribute
        """

        return (self.__size)
