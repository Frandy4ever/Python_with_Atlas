#!/usr/bin/env python3

"""
This program will print and or return the last digit
of a signed integer given to the param.
"""
def print_last_digit(number: int) -> int:
    """Prints the last digid of `number` value."""
    print(number % 10, end='')
    
    """Returns the last digit of `number` value."""
    return (number % 10)
