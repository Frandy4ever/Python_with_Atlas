#!/usr/bin/env python3

"""This program will print all integer of a list in reverse order"""
from typing import List
def print_reversed_list_integer(my_list: List[int] = []) -> None:
    for n in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[n]))
