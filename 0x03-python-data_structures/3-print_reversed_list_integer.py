#!/usr/bin/python3
# a script to print all elems ofa list in reverse

def print_reversed_list_integer(my_list=[]):
    for i in (my_list[::-1]):
        print("{:d}".format(i))
