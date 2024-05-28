#!/usr/bin/env python3

"""This module will generate new files using the provided list elements."""
from typing import List
import os

# Files names
files: List[str] = [
    '0-square_matrix_simple.py', '1-search_replace.py', '2-uniq_add.py',
    '3-common_elements.py', '4-only_diff_elements.py', '5-number_keys.py', '6-print_sorted_dictionary.py',
    '7-update_dictionary.py', '8-simple_delete.py', '9-multiply_by_2.py', '10-best_score.py',
    '11-multiply_list_map.py', '12-roman_to_int.py', '100-weight_average.py',
    '101-square_matrix_map.py', '102-complex_delete.py'
]

def create_files(list: List[str]) -> None:
    for file in list:
        with open(file, 'w') as f:
            f.write('#!/usr/bin/env python3')
            os.chmod(file, 0o755)

create_files(files)
