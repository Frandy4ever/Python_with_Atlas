#!/usr/bin/env python3

"""This program deletes keys with a
specific value in a dictionary."""

from typing import Dict, Union


def complex_delete(a_dictionary: Dict[int, str],
                   value: Union[int, str]) -> Dict[int, str]:
    """Delete a value from a_dictionary if it exist"""
    temp_dict = a_dictionary.copy()
    
    for k, v in temp_dict.items():
        if value == v:
            del a_dictionary[k]
    
    return a_dictionary
