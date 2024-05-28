#!/usr/bin/env python3

"""This program returns the number of keys in a dictionary"""

from typing import Dict

# return (len(a_dictionary.keys()))
def number_keys(a_dictionary: Dict[int, str]) -> int:
    """Returns the number of a_dictionary keys"""
    return len(a_dictionary)
