#!/usr/bin/python3
# a script to print lowercase chars using ascii
for i in range(97, 123):
    if (chr(i) == 'q' or chr(i) == 'e'):
        continue
    print("{}".format(chr(i)), end="")
