#!/usr/bin/python3
# make sorted dict

def print_sorted_dictionary(a_dictionary):
    pr = sorted(a_dictionary)
    for k, v in pr.items():
        print(f"{k}: {v}")
