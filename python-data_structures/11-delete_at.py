#!/usr/bin/env python3

"""This program deletes the item at a specific position in a list."""
from typing import List


def delete_at(my_list: List[int] = [], idx: int = 0) -> List[int]:
    """Return a the my_list modified"""
    if len(my_list) < idx or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
