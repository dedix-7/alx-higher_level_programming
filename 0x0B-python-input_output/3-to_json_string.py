#!/usr/bin/python3
""" The module to return a json representation of an object
"""
import json


def to_json_string(my_obj):
    """ Function to convert oject to json string
        The function does not account for any execpetions
        Args: obj, object to e converetd
    """

    return (json.dumps(my_obj))
