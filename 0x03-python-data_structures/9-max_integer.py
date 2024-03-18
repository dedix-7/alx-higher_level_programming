#!/usr/bin/python3
# A script to find the largest integer in a list

def max_integer(my_list=[]):
    if (my_list == []):
        return None
    large = my_list[0]
    for r in my_list:
        if (r > large):
            large = r
