#!/usr/bin/python3
# print ints alone

def safe_print_list_integers(my_list=[], x=0):
    # function to print the ints
    num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print()
    return (num)
