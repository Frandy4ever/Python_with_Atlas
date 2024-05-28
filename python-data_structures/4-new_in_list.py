#!/usr/bin/env python3

"""This program replaces an element in a list at a
specific position without modifying the original list.
"""
from typing import List, Union

def new_in_list(my_list: List[Union[int, str]], idx: int,
                element: Union[int, str]) -> List[Union[int, str]]:
    """Generate a copy of my_list"""
    my_new_list = [*my_list]
    if 0 <= idx < len(my_new_list):
        my_new_list[idx] = element
    return my_new_list
