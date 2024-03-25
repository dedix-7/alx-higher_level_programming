#!/usr/bin/python3
# A script to calculate the weighted average

def weight_average(my_list=[]):
    if (my_list):
        if (type(my_list) is not list):
            return (0)
        sums, aver, weight = 0, 0, 0
        for tup in my_list:
            prod = 1
            for num in tup:
                prod *= num
            sums += prod
            weight += tup[1]
        return ((sums) / (weight))
    else:
        return (0)
