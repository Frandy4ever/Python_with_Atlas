#!/usr/bin/env python3
"""
This program imports calculator_1 module as cal
and makes use of its functionalities.
"""
if __name__ == ('__main__'):
    from calculator_1 import add, sub, mul, div

    a: int = 10
    b: int = 5

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
