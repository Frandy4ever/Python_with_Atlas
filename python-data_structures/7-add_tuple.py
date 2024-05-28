#!/usr/bin/env python3
"""This program adds 2 tuples"""
from typing import Tuple


def add_tuple(tuple_a: Tuple[int, ...]=(),
              tuple_b: Tuple[int, ...] = ()) -> Tuple[int, int]:
    """"Returns the sum of two tuples"""
    a1, a2 = (tuple_a + (0, 0))[:2]
    b1, b2 = (tuple_b + (0, 0))[:2]
    return (a1 + b1, a2 + b2)
