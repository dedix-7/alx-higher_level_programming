#!/usr/bin/python3
""" A module to return the object given as json to original object
"""
import json as j


def from_json_string(my_str):
    """ Function to reresent the given string as original object
    Args:
         my_str: string representation
    """

    return (j.loads(my_str))
