#!/usr/bin/python3
# a script to solve the fizz buzz problem in python

def fizzbuzz():
    x = 3
    y = 5
    for dig in range(1, 101):
        if ((dig % x) == 0 and (dig % y) == 0):
            print(f"FizzBuzz", end=" ")
        elif (dig % x) == 0:
            print(f"Fizz", end=" ")
        elif (dig % y) == 0:
            print(f"Buzz", end=" ")
        else:
            print(f"{dig}", end=" ")
