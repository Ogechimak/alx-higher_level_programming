#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 0 else (number * -1) % 10
if last_digit > 5:
    print(f"last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"last digit of {number} is {last_digit} and is 0")
elif (number < 0 or last_digit < 6):
    if (number < 0):
        print(f"last digit of {number} is -{last_digit} and is less than 6 annd not 0")