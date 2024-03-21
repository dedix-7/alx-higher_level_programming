#!/usr/bin/python3
# a script to delete a gicen key

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
