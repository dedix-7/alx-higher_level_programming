#!/usr/bin/python3
""" Mosule to write to a file
"""


def append_write(filename="", text=""):
    """ Function to write to files
         Args:
              filename: file path to write to
              text: text to write to gicen file
    """

    with open(filename, mode='a', encoding="utf-8") as fd:
        return (fd.write(text))
