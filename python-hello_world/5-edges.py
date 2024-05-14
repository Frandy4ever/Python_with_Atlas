#!/usr/bin/env python3

"""
This code prints the first 3 letters of the string contained
in word variable, then it prints the last two letters 
follow by printing all letter except the first and last letters
"""
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]

print(word_first_3, word_last_2, middle_word)
