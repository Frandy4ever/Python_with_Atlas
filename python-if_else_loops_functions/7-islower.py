#!/usr/bin/env python3

"""
This program will eval if aa given Ascii alphabet
character is in lowercase of uppercase.
"""

def isLower(c: chr) -> bool:
    return ord('a') <= ord(c) <= ord('z')

if __name__ == "__main__":
    print(isLower('p'))
