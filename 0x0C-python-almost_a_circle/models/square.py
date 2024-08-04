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
        """ Getter for the size attribute
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

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if kwargs is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ a function to return the dictionary representation of a rectangle
        """

        return {'id': self.__id, 'size': self.__size, 'x': self.__x,
                'y': self.__y}
