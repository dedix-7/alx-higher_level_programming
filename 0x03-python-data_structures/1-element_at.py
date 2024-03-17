#!/usr/bin/python3
# a module to retrive an index element

def element_at(my_list, idx):
    if (idx >= len(my_list)):
        return None
    if (idx < 0):
        return None
    return (my_list[idx])
