#!/usr/bin/python3
# a script to print numbers till 99

for i in range(100):
    if (i < 99):
        print("{:0>2}".format(i), end=", ")
    elif (i == 99):
        print("{:2}".format(i))
