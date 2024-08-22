#!/usr/bin/python3
""" Mosule to write to a file
"""


def write_file(filename="", text=""):
    """ Function to write to files
         Args:
              filename: file path to write to
              text: text to write to gicen file
    """

    with open(filename, mode='w', encoding="utf-8") as fd:
        return (fd.write(text))
