#!/usr/bin/env python3

"""
This program will print the Ascii alphabet in lowercase
skipping 'e' and 'q'.
"""
for char in range(ord('a'), ord('z') + 1):
    char = chr(char)
    if char not in ['e', 'q']:
        print(char, end='')
