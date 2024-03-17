#!/usr/bin/python3
# a module to replace an lement in a copy

def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    if (idx < 0):
        return my_list[:]
    if (idx >= len(my_list)):
        return my_list[:]
    new = my_list[:]
    new[idx] = element
    return (new)
