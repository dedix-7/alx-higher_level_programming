#!/usr/bin/python3
# Clone the inbuilt pop functions

def delete_at(my_list=[], idx=0):
    if ((idx < 0) or (idx >= len(my_list))):
        return (my_list)
    new = []
    for i in range(len(my_list)):
        if (i == idx):
            continue
        else:
            new.append(my_list[i])
    return (new)
