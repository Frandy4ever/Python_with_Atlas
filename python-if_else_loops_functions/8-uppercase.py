#!/usr/bin/env python3
"""
This program will convert every Ascii characters
between 'a' and 'z' inclusive, found within 
`str` param to uppercase.
"""
def isUpper(str: str) -> None:
    for i in str:
        i = ord(i)
        if ord('a') <= i <= ord('z'):
            i -= 32
        print(chr(i), end='')
    print()
