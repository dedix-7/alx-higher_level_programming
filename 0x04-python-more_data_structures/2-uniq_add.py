#!/usr/bin/python3
# add all unique elements in a list

def uniq_add(my_list=[]):
    # I'll use set instaed of making a new list
    check = set(my_list)
    psum = 0
    for i in check:
        psum += i
    return (psum)
