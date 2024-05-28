#!/usr/bin/env python3

"""This program returns a set of common elements in two sets."""

from typing import Set, Union


def common_elements(set_1: Set[Union[int, str]],
                    set_2: Set[Union[int, str]]) -> Set[Union[int, str]]:
    """Returns what's common between two sets."""
    return [elm1 for elm1 in set_1 for elm2 in set_2 if elm1 == elm2]
