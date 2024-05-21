#!/usr/bin/env python3

"""
This program will print the Ascii alphabet
in reversed order alternating lowercase and
uppercase letters.
"""

for i in range(ord('z'), ord('a') -1, -1):
    print(chr(i - 32) if i % 2 == 1 else chr(i), end='')
