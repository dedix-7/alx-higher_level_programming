#!/usr/bin/python3
""" A module to return dictionary descripon for json serial
"""


def class_to_json(obj):
    """ A function that returns the dictionary description
    of an object
    """

    return (obj.__dict__)
