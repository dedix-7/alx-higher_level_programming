#!/usr/bin/python3
# a module to check commandline arguments
import sys
length = len(sys.argv)
if __name__ == "__main__":
    if (length == 1):
        print("0 arguments.")
    elif (length == 2):
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{length - 1} arguments:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
