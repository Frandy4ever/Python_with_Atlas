#!/usr/bin/env python3

"""This program  adds all unique integers in a list"""
from typing import List

def uniq_add(my_list: List[int]) -> int:
    """Returns the sum of unique integers in my_list"""
    return sum(set(my_list))
