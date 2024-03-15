#!/usr/bin/python3
# a moduel to rpint all combinations pf 2 digit numebrs with
# It only uses 2 loops

for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if (digit1 == 8 and digit2 == 9):
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
