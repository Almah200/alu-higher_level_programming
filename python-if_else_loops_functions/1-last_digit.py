#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = repr(number)
last_digit_number = new_number[-1]
last_digit = int(last_digit_number)
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif (last_digit < 6) or (last_digit != 0):
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
