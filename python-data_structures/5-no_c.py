#!/usr/bin/env python3

"""This program removes all characters c and C from a string."""

def no_c(my_string: str) -> str:
    """Remove all 'c' and 'C' from a string."""
    new_str = ''.join([char for char in my_string
                       if char != 'c' and char != 'C'])
    return new_str
