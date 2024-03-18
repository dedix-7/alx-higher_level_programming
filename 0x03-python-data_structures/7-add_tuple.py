#!/usr/bin/python3
# a script to add 2 tuples

def add_tuple(tuple_a=(), tuple_b=()):
    """ A function to add tuples enforcing 2 tuples
    """

#!/usr/bin/python3
# add two tuples


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a += (0,)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b += (0,)
    sum_tuple1 = tuple_a[0] + tuple_b[0]
    sum_tuple2 = tuple_a[1] + tuple_b[1]
    return (sum_tuple1, sum_tuple2)
