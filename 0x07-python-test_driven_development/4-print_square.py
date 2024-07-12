#!/usr/bin/python3
""" A script to ptint a square
"""


def print_square(size):
    """ A function to print a square using the # char

        Args:
             Size - size of the sqaure
        Raises:
             TypeError for non-integr values
             ValueError - for ints less than 0
        Return:
              None
    """

    if (type(size) is not int):
        raise TypeError('size must be an integer')
    if (size < 0):
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
