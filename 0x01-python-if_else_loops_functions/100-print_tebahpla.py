#!/usr/bin/python3
# a module to print lowercase n uppercase chars

check = 0
for letter in range(122, 96, -1):
    print("{}".format(chr(letter - check)), end="")
    check = 32 if check == 0 else 0
