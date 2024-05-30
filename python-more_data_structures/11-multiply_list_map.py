#!/usr/bin/env python3
"""This program returns a list with all values
multiplied by a number without using any loops"""
from typing import List


def multiply_list_map(my_list: List[int]=[], number: int=0) -> List[int]:
    """Return. a new modified list."""
    return list(map(lambda i: i * number, my_list))
