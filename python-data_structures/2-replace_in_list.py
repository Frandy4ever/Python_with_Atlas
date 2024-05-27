#!/usr/bin/env python3

"""This program replaces an element of a list at a specific position"""
from typing import  Union, List
def replace_in_list(my_list: List[Union[int, str]],
                    idx: int, element: Union[int, str]) -> List[Union[int, str]]:
    """Replace element at a given index"""
    if 0 <= idx < len(my_list):
       my_list[idx] = element
        
    return my_list
