#!/usr/bin/env python3

"""This program returns a new dictionary
with all values multiplied by 2"""
from typing import Dict


def multiply_by_2(a_dictionary: Dict[str, int]) -> Dict[str, int]:
    """Returns a copy of a_dictionary with each value multiplied by 2"""
    return {key: val * 2 for key, val in a_dictionary.items()}
