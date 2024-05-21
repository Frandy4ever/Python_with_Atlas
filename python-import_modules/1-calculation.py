#!/usr/bin/env python3
"""
This program imports calculator_1 module as cal
and makes use of its functionalities.
"""
if __name__ == ('__main__'):
    import calculator_1 as cal

    a: int = 10
    b: int = 5

    print(f"{a} + {b} = {cal.add(a, b)}")
    print(f"{a} - {b} = {cal.sub(a, b)}")
    print(f"{a} * {b} = {cal.mul(a, b)}")
    print(f"{a} / {b} = {cal.div(a, b)}")
