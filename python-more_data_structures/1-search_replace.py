#!/usr/bin/env python3
"""This program replaces all occurrences of
an element by another in a new list."""

from typing import List

def search_replace(my_list: List[int], search: int, replace: int) -> List[int]:
    """Returns a new list where search is replaced by replace"""
    return [replace if i == search else i for i in my_list]
