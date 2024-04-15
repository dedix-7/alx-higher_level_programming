#!/usr/bin/python3
# make reverseed fuinction
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception("Too far")
            result += ((a ** b) / i)
    result += a + b
    return (result)
