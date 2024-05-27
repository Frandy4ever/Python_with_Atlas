#!/usr/bin/env python3

"""This program prints all integer elements of a list"""
from typing import List
def print_list_integer(my_list: List[int] = []) -> None:
    """Print all elements of my_list"""
    for n in my_list:
        print("{:d}".format(n))
