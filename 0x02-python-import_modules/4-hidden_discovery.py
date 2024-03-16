#!/usr/bin/python3
# a script to print names defined in a given module

import hidden_4
if __name__ == "__main__":
    for word in dir(hidden_4):
        if (word[:2] == "__"):
            continue
        print(word)
