#!/usr/bin/python3
# a script to print names defined in a given module

import hidden_4
for word in dir(hidden_4):
    if (word[:2] == "__"):
        continue
    print(word)
