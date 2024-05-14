#!/usr/bin/env python3

"""
This code will print the value of str variable 3 times, then
it will print the first 5 characters of the same variable
"""
str: str = "Atlas School"

print("{}".format(str * 3))
print(str[:5]) # Use of slice
