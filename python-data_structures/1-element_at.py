#!/usr/bin/env python3

"""This program retrieves an element from a list"""
from typing import Union
def element_at(my_list: Union[int, str], idx: int) -> Union[None, int]:
    """Print element at a given index"""
    if idx < 0 or idx > len(my_list):
        return None
    else:
        return my_list[idx]
