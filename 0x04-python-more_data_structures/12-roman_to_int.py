#!/usr/bin/python3
# a script to convert roman numerals to ints

def roman_to_int(roman_string):
    if ((roman_string is None) or (type(roman_string) is not str)):
        return (0)
    res = 0
    check = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for c in (range(len(roman_string))):
        curr = check.get(roman_string[c])
        if (c):
            prev = check.get(roman_string[c - 1])
            if (curr > prev):
                res -= prev
                res += (curr - prev)
                continue
            else:
                res += curr
                continue
        res += curr
    return (res)
