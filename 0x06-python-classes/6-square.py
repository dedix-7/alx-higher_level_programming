#!/usr/bin/python3
""" This project os to defne a simple sqaure class
"""


class Square:
    """ The definition fr the quare class
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Instantiating the size of the class
        """

        if ((type(size)) is not int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
        if (type(position) is not tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (len(position) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (type(position[0]) is not int or type(position[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    @property
    def size(self):
        """ Getter for the size attribute
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """ A method setter for the soze attriute
        """

        if ((type(value)) is not int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ A ,ethod to return the area of he square
        """

        return (self.__size * self.__size)

    def my_print(self):
        """ function to print the square

        Args:
              self - instance
        """

        for u in range(self.__position[1]):
            print()
        if (self.__size == 0):
            print()
            return
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """ Position getter
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        """ Setter for the position attribute
        """

        if (type(value) is not tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (len(value) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if (value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
        return (self.__position)
