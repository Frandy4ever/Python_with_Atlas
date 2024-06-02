#!/usr/bin/env python3

"""This program returns the weighted average of all integers tuple."""
from typing import List


def weight_average(my_list: List[int]) -> int:
    """Return the a tuple weight average."""

    # Sum of total weight
    weight_total: int = sum(weight for value, weight in my_list)
    # Sum of weights times values
    weight_sum: int = sum(weight * value for value, weight in my_list)
    # Get average
    result: float = weight_sum / weight_total

    return result
