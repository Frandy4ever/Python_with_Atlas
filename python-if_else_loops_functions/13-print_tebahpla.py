#!/usr/bin/env python3

"""
This program will print the Ascii alphabet
in reversed order alternating lowercase and
uppercase letters.
"""

for i in range(ord('z'), ord('a') -1, -1):
    if i % 2 == 1:
        i -= 32
        print(chr(i), end='')
    else:
        print(chr(i), end='')
