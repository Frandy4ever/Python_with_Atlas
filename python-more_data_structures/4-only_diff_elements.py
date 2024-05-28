#!/usr/bin/env python3

"""This program returns a set of all elements present in only one set."""
from typing import Set

def only_diff_elements(set_1: Set[str], set_2: Set[str]) -> Set[str]:
    """Returns unique elements between two sets."""
    return set_1 | set_2
