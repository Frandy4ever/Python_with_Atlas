#!/usr/bin/env python3
"""
This program imports add_0 module and uses its add() fn to print the sum of `a` and `b`.
"""
if __name__ == ("__main__"):
    from add_0 import add
    """Print the sum of a and b"""
    a: int = 1
    b: int = 2

    print("{} + {} = {}".format(a, b, add(a, b)))
