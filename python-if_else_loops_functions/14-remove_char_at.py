#!/usr/bin/env python3

"""
This program will remove character at `n` index
of a copy of a given string.
"""
def remove_char_at(str: str, n: int) -> str:
    """Return new string without the value
    at n index"""
    new_str = ''.join([str[i] for i in range(len(str)) if str[i] is not n])
    
    return new_str
