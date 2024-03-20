#!/usr/bin/python3
# change a particular element

def search_replace(my_list, search, replace):
    # Function to replace
    replac = []
    for i in range(len(my_list)):
        if (my_list[i] == search):
            replac.append(replace)
            continue
        replac.append(my_list[i])
    return (replac)
