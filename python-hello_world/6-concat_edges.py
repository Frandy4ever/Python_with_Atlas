#!/usr/bin/env python3

"""
This program will take particular parts of a given string
to form a new string and print its value, using string format.
"""
str = "Python is an interpreted, interactive, object-oriented programming\
    language that combines remarkable power with very clear syntax"

new_str = str[39:66] +" "+ str[110:114] +" "+ str[:6]
print("{}".format(new_str))
