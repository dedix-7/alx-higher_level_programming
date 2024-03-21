#!/usr/bin/python3
# a script to get the biggest score

def best_score(a_dictionary):
    if (a_dictionary):
        return (max(zip(a_dictionary.values(), a_dictionary.keys()))[1])
