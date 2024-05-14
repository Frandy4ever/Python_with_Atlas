#!/usr/bin/env python3

"""The variable number will store a different value every time you will run this program.
The output of the program will be:
The string `Last digit of`, followed by
`the number`, followed by
the string `is`, followed by the last digit of number, followed by
if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0"""

import random

number = random.randint(-10000, 10000)
number = abs(number)
if number % 10 > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, number % 10))
elif number % 10 == 0:
    print("Last digit of {} is {} and is 0".format(number, number % 10))
elif number % 10 < 6 and number % 10 != 0:
    print("Last digit of {} is {} and is less than 6 and is not 0".format(number, number % 10))
