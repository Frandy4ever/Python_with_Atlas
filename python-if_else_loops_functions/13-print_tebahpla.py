#!/usr/bin/env python3

"""
This program will remove character at `n` index
of a copy of a given string.
"""
def remove_char_at(str: str, n: int) -> None:
    """Return new string without the value
    at n index"""
    for i in range(len(str)):
        if i == n:
            continue
        print(str[i], end='')
    print()
