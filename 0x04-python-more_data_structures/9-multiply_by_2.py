#!/usr/bin/python3
# a script to udate values and return new dict

def multiply_by_2(a_dictionary):
    vals = [(a * 2) for a in a_dictionary.values()]
    keys = [k for k in a_dictionary.keys()]
    newdic = {keys[i]: vals[i] for i in range(len(keys))}
    return (newdic)
