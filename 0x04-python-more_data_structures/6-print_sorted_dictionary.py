#!/usr/bin/python3
# make sorted dict

def print_sorted_dictionary(a_dictionary):
    pr = sorted(a_dictionary)
    ret = {pr[i]: a_dictionary.get(pr[i]) for i in range(len(pr))}
    for k, v in ret.items():
        print(f"{k}: {v}")
    return (ret)
