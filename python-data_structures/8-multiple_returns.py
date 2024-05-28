#!/usr/bin/env python3
"""This program returns a tuple with the
length of a string and its first character."""
from typing import Tuple


def multiple_returns(sentence: str) -> Tuple[int, chr]:
    """Returns the length value and last char of sentence."""
    return (len(sentence), sentence[0])
