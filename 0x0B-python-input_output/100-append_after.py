#!/usr/bin/python3
""" A module to append text after a given string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function to append the text
    Args:
    filename: path to file
    search_string: string to append after
    new_string: string to append
    """

    text = ''
    with open(filename, 'r+', encoding="utf-8") as fildes:
        for lin in fildes:
            text += lin
            if (search_string in lin):
                text += new_string
    with open(filename, 'w', encoding='utf-8') as fildes:
        fildes.write(text)
