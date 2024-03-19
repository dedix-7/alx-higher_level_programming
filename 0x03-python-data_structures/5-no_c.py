#!/usr/bin/python3
# a module to remove

def no_c(my_string):
    if my_string is None:
        return None
    new = ''
    for letter in my_string:
        if (letter == 'c' or letter == 'C'):
            continue
        new += letter
    return (new)
