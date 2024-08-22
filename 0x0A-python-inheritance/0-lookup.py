#!/usr/bin/python3
""" This module seeks to write attributes and methods opf an object
"""


def lookup(obj):
    """This function returns said modeuls as an object
    """

    return ([att for att in dir(obj)])
