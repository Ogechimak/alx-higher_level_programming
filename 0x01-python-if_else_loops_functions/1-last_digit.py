#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
L_d = (number % 10) if number > 0 else (number * -1) % 10
if (L_d > 5 and number > 0):
    print(f"last digit of {number} is {L_d} and is greater than 5")
elif L_d == 0:
    print(f"last digit of {number} is {L_d} and is 0")
elif (number < 0 or L_d < 6):
    if (number < 0):
        print(f"last digit of {number} is -{L_d} and is less than 6 annd not 0")
