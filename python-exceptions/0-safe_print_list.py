#!/usr/bin/env python3

"""This program prints x elements of a list."""
from typing import List


def safe_print_list(my_list: List[int]=[], x: int=0) -> int:
    """Print elements x amount of time"""
    elm_count: int = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            elm_count += 1
        except IndexError:
            break
    print()
    return elm_count
