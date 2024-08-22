#!/usr/bin/python3
""" A module to load a json file to its original object
"""


def load_from_json_file(filename):
    """ function to load the given json file
    Args:
        filename: file to convert cotents of
    """

    with open(filename, encoding="utf-8") as fildes:
        import json
        data = fildes.read()
        return (json.loads(data))
