#!/usr/bin/env python3
"""
This program will generate new files, add the Shebang line to them
and give them execution permissions.
"""
from typing import List
import os

files = [
    '0-add.py', '1-calculation.py', '2-args.py', '3-infinite_add.py', '5-variable_load.py',
    '100-my_calculator.py', '101-easy_print.py', '102-magic_calculation.py', '103-fast_alphabet.py'
]


def generate_files(array: List[str]) -> None:
    """Generate new files with execution permissions."""
    for file in array:
        with open(file, 'w', encoding='utf-8') as f:
            f.write('#!/usr/bin/env python3\n')
            # Add execution permissions
            os.chmod(file, 0o755)

generate_files(files)
