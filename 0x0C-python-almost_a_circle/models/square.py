#!/usr/bin/python3
""" A modyule for creating squares
"""


import rectangle

class Square(rectangle.Rectangle):
    """ A class for the suqare object
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for the square class
            It is a special rectangle
        """

        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """ what to write when retur ning this object\
        """

        return f"[Square] ({self.__id}) {self.__x}/{self.__y} - {self.__size}"

    @size.setter
    def size(self, value):
        
