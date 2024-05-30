#!/usr/bin/env python3computes the square value ofall integers of a matrix using map
"""This program computes the square value
of all integers of a matrix using map"""
from typing import List


def square_matrix_map(matrix: List[List[int]]) -> List[List[int]]:
    """Returns the square of element in the matrix"""
    return [[num * num for num in row] for row in matrix]
            