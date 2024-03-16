#!/usr/bin/python3
# a module to remove a char at a position in a string

def remove_char_at(str, n):
    if (n < 0):
        return (str)
    return (str[:n] + str[n+1:])
