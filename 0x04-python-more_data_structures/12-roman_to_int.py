#!/usr/bin/python3
# a script to convert roman numerals to ints

def roman_to_int(roman_string):
    if (!roman_string):
        return (0)
    res = 0
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for c in (range(len(roman_string))):
        val = roman_string[c]
        val1 = 0
        if c >= len(roman_string):
            val1 = roman_string[c + 1]
        if (val1):
            if (val1 > val)
