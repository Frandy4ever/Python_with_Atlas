#!/usr/bin/env python3
"""This program deletes a key in a dictionary."""
from typing import Dict


def simple_delete(a_dictionary: Dict[int, str], key: str = ''):
    """Returns a modified dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
