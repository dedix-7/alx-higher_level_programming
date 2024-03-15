#!/usr/bin/python3
# A script to print the last digit of a number

def print_last_digit(number):
    if (number < 0):
        num = -1 * number
        print("{}".format(num % 10))
        return (num % 10)
    else:
        print("{}".format(number % 10))
        return (number % 10)
