#!/usr/bin/python3
# a script to delte dictionary values

def complex_delete(a_dictionary, value):
    if (a_dictionary):
        keys = []
        for k, v in a_dictionary.items():
            if (v == value):
                keys.append(k)
        for u in keys:
            del a_dictionary[u]
    return (a_dictionary)
