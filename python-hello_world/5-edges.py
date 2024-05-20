#!/usr/bin/env python3

"""
This program prints the first 3 letters of a given string variable,
then it prints the last two letters followed by printing all letters
but the first and last letters of the same string, using string format.
"""
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]

print("{}\n{}\n{}".format(word_first_3, word_last_2, middle_word))
