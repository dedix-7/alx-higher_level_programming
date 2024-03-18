#!/usr/bin/python3
# a script to add 2 tuples

def add_tuple(tuple_a=(), tuple_b=()):
    """ A function to add tuples enforcing 2 tuples
    """

    e = None
    one = ()
    two = ()
    for i in range(2):
        try:
            tuple_a[i]
        except exception as p:
            e = "some index error"
        if (e):
            one += (0,)
        else:
            one += (tuple_a[i],)
    e = None
    for r in range(2):
        try:
            tuple_b[r]
        except IndexError as p:
            e = "some error"
        if (e):
            two += (0,)
        else:
            two += (tuple_b[r],)
    ret = ((one[0] + two[0]), (one[1] + two[1]))
    return (ret)
