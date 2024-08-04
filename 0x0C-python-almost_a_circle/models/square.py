#!/usr/bin/python3
""" A modyule for creating squares
"""


from models import rectangle


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

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ Getter for teh size attribute
        """

        return (self.__size)

    @rectangle.Rectangle.width.setter
    def size(self, value):
        """ a setter for the size attribute, inheriting from that of rcevtangle
        """
        super(Square, Square).width.__set__(self, value)

    def update(self, *args, **kwargs):
        """ method to update the attributes
        """

        attributes = [self.id, self.__size, self.__x, self.__y]
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

        return {'id': self.__id, 'size': self.__size, 'x': self.__x,
                'y': self.__y}
