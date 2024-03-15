#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
dig = math.fmod(number, 10)
dig = int(dig)
print(f"Last digit of {number} is {dig} ", end=" ")
if (dig > 5):
    print("and is greater than 5")
elif (dig == 0):
    print("and is 0")
elif ((dig < 6) and (dig != 0)):
    print("and is less than 6 and not 0")
