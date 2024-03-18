#!/usr/bin/python3
# A script to find even numbers

def divisible_by_2(my_list=[]):
    if (my_list):
        new = []
        for r in my_list:
            if ((r % 2) == 0):
                new.append(True)
            else:
                new.append(False)
        return (new)
