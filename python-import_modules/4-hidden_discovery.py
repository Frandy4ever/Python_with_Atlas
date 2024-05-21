#!/usr/bin/env python3

"""
This program will print all the names defined by the compiled
module, hidden_4.pyc except names beginning with double under score.
"""

import hidden_4
from typing import List


def get_names() -> None:
    """Prints the name of files that don't start with double under score."""
    names: List[str] = dir(hidden_4)
    filtered_names: List[str] = sorted(name for name in names if not name.startswith('__'))
    
    for name in filtered_names:
        print(name)

if __name__ == ('__main__'):
    get_names()
