#!/usr/bin/env python3

"""This program replaces or adds key/value in a dictionary."""
from typing import Union, Dict


def update_dictionary(a_dictionary: Dict[int, str],
                      key: str, value: Union[int, str]) -> Dict[int, str]:
    """Update key and or value when possible."""
    a_dictionary[key] = value
    return a_dictionary
