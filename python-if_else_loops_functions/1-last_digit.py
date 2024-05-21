#!/usr/bin/env python3

"""
This program will assign random signed number to `number` variable,
it print a unique message for when the last digit of the number
is zero, greater than 5 or less than six and is not zero.
"""

import random

number: int = random.randint(-10000, 10000)
digit: int = abs(number) % 10

if number < 0:
  digit = -digit
if digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, digit))
elif digit == 0:
    print("Last digit of {} is {} and is 0".format(number, digit))
elif digit < 6 and digit != 0:
    print("Last digit of {} is {} and is less than 6 and is not 0".format(number, digit))
