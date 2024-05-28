#!/usr/bin/env python3

"""This program finds the biggest integer of a list."""
from typing import List


def max_integer(my_list: List[int] = []) -> int:
    """Return the greatest number of my_list."""
    if len(my_list) <= 0:
        return None
    
    max_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num
