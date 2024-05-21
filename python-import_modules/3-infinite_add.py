#!/usr/bin/env python3

import sys
from typing import List

"""
This program will print sum of all args.
"""

def add_args() -> None:
    """Computes the sum of all arguments"""
    args: List[str] = sys.argv[1:]
    result: int = 0
    for i in args:
        result += int(i)
    
    print(result)

if __name__ == ('__main__'):
    add_args()
