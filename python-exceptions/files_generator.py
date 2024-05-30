#!/usr/bin/env python3

"""This module will generate new files using the provided list elements."""
from typing import List
import os

# Files names
files: List[str] = [
    '0-safe_print_li', '1-safe_print_integer.py',
    '2-safe_print_list_integers.py', '3-safe_print_division.py',
    '4-list_division.py', '5-raise_exception.py',
    '6-raise_exception_msg.py', '100-safe_print_integer_err.py',
    '101-safe_function.py', '102-magic_calculation.py'
]

def create_files(list: List[str]) -> None:
    for file in list:
        with open(file, 'w') as f:
            f.write('#!/usr/bin/env python3')
            os.chmod(file, 0o755)

create_files(files)
