#!/usr/bin/env python3

"""This program prints all integer elements of a list"""
from typing import List
def print_list_integer(my_list: List[int] = []) -> None:
    for n in my_list:
        print("{}".format(n))
