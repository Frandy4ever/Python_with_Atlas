#!/usr/bin/env python3
"""This program prints an integer with "{:d}".format()."""
from typing import Union


def safe_print_integer(value: Union[int, str]) -> bool:
    """Return boolean value if value is integer or not."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
