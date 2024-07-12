#!/usr/bin/python3
""" this module tests whether I can use blanklines in my test
"""


def text_indentation(text):
    """ A funtion to print a text with 2 new lines after .? :
        Args:
           text - text to format
        Raises:
           TypeError - if the text is not a string
    """

    if (type(text) is not str):
        raise TypeError('text must be a string')
        count = 0
    for e in text:
        if (e in ['.', '?', ':']):
            print(e)
            count = 1
            print()
            count = 1
            continue
        elif (e == ' '):
            if (count == 1):
                continue
            else:
                print(e, end='')
                count = 0
        else:
            print(e, end='')
            count = 0
            continue
