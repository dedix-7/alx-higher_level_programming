#!/usr/bin/python3
# A script to print a char and strlen

def multiple_returns(sentence):
    length = len(sentence)
    if (length == 0):
        char = None
    else:
        char = sentence[0]
    return (length, char)
