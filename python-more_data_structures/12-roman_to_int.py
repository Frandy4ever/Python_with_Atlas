#!/usr/bin/env python3

"""This program converts a Roman numeral to an integer."""

def roman_to_int(roman_string: str) -> int:
    """Returns roman numerals converted to integers"""

    # Mapping roman characters to integer
    roman_numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    # Initialize previous value and total
    prev_value = 0
    total = 0

    # Iterate over roman numeral right to left
    for char in reversed(roman_string):
        # Get the integer value
        value = roman_numerals[char]

        # Apply subtraction rule
        if value < prev_value:
            total -= value
        else:
            total += value
    return total
