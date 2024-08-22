#!/usr/bin/python3
""" A module to write an object to a text file
It uses json reorsentation
"""


def save_to_json_file(my_obj, filename):
    """ a function to save it to the file
    Args:
          my_obj: object
          filename: file to write to
    """

    with open(filename, "w", encoding="utf-8") as fildes:
        import json
        fildes.write(json.dumps(my_obj))
