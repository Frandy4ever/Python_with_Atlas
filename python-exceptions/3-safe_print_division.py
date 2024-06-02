#!/usr/bin/env python3
"""This program divides 2 integers and prints the result."""


def safe_print_division(a, b):
    """Handle Zero division error"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
