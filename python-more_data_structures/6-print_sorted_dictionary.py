#!/usr/bin/env python3

"""This program prints a dictionary by ordered keys"""
from typing import Dict


def print_sorted_dictionary(a_dictionary: Dict[int, str]) -> Dict[int, str]:
    """Returns a dictionary sorted by keys."""
    return {key: a_dictionary[key] for key in sorted(a_dictionary)}
