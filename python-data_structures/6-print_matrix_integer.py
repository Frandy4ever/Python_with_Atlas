#!/usr/bin/env python3

"""This program prints a matrix of integers."""
from typing import List
def print_matrix_integer(matrix: List[List[int]]) -> int:
    for row in matrix:
        print("\n")
        for elm in row:
            print(elm, end=" ")
