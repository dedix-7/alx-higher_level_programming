#!/usr/bin/python3
# a script to solve the fizz buzz problem in python

def fizzbuzz():
    x = 3
    y = 5
    for dig in range(1, 101):
        if ((dig % x) and (dig % y)):
            print(f"FizzBuzz")
        elif (dig % x):
            print (f"Fizz")
        elif (dig % y):
            print(f"Buzz")
        else:
            print(f"{dig}")
