#!/usr/bin/env python3
"""This program computes the square value of all integers of a matrix. """
from typing import List


def square_matrix_simple(matrix: List[List[int]] = []) -> List[List[int]]:
    """Returns the square value of each element in the matrix"""
    return [[elm * elm for elm in row] for row in matrix]
