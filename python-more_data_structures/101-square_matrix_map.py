#!/usr/bin/env python3computes the square value ofall integers of a matrix using map
"""This program computes the square value
of all integers of a matrix using map"""
from typing import List


def square_matrix_map(matrix: List[List[int]]) -> List[List[int]]:
    """Returns the square of element in the matrix"""
    return list(map(lambda row: list(map(lambda num: num ** 2, row)), matrix))
 