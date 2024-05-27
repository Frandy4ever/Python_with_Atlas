#!/usr/bin/env python3

import os

files = [
    "0-print_list_integer.py", "1-element_at.py",
    "2-replace_in_list.py", "3-print_reversed_list_integer.py",
    "4-new_in_list.py", "5-no_c.py", "6-print_matrix_integer.py",
    "7-add_tuple.py", "8-multiple_returns.py", "9-max_integer.py",
    "10-divisible_by_2.py", "11-delete_at.py", "12-switch.py"
]

for file in files:
    with open(file, 'w') as f:
        f.write("#!/usr/bin/env python3")
        os.chmod(file, 0o755)
