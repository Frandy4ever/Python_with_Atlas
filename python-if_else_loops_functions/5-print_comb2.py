#!/usr/bin/env python3

"""
This program will print decimal numbers from 0 through
99 separated by comma. All numbers will be printed as two
digits number.
"""

for i in range(100):
  if i != 99:
    print(f'{i:02},', end=' ')
  else:
    print(i)
