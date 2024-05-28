#!/usr/bin/env python3
"""This program finds all multiples of 2 in a list."""
from typing import List


def divisible_by_2(my_list: List[int] = []) -> List[bool]:
    """Check if list elements are divisible by 2 or not."""
    new_list = [i % 2 == 0 for i in my_list]
    return new_list

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)
