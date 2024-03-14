#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {number % 10}", end=" ")
dig = number % 10
if (dig > 5):
    print(f"and is greater than 5")
elif (dig == 0):
    print(f"and is 0")
elif ((dig < 6) and (dig != 0)):
    print(f"and is less than 6 and not 0")
