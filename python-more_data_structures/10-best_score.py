#!/usr/bin/env python3

"""This program returns a key with the biggest integer value."""
from typing import Dict


def best_score(a_dictionary: Dict[str, int]) -> int:
    """Returns the greatest score."""
    max_score = 0
    result = ""
    if not a_dictionary:
        return None

    for k, v in a_dictionary.items():
        if v > max_score:
            max_score = v
            result = k
    return result
