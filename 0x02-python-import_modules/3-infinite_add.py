#!/usr/bin/python3
# a module to add all given arguments

import sys
lengt = len(sys.argv)
num = 0
if __name__ == "__main__":
    if (lengt > 1):
        for i in (sys.argv[1:]):
            num += int(i)
        print(f"{num}")
