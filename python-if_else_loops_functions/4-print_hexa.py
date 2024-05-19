#!/usr/bin/env python3

"""
This program print decimal numbers from 0 through 98
alongside their hexadecimal equivalent.
"""

for n in range(99):
    print("{} = 0x{:x}".format(n, n))
