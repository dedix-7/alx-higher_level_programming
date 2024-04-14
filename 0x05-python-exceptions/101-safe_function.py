#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    # a funtion to return others
    try:
        res = fct(*args)
    except Exception as mess:
        print("Exception: {}".format(mess), file=sys.stderr)
        return
    return res
