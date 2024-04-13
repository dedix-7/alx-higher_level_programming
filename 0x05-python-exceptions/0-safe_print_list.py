#!/usr/bin/python3
# a script to check exceptions in a list

def safe_print_list(my_list=[], x=0):
    # the function to print
    tot = 0
    for i in range(0, x):
        try:
            y = mylist[i]
            print(y, end="")
            tot += 1
        except(IndexError):
            break
    return (num)
