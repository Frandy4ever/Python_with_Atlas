#!/usr/bin/env python3

"""
This code will print the value of a string variable 3 times, then
it will print the first 5 characters of the same string, using string format.
"""
str: str = "Atlas School"

print("{}".format(str * 3))
print("{}".format(str[:5])) # Use of slice
