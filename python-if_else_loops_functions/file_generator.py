#!/usr/bin/env python

"""
This script when run, will create the files in the files list,
and add a shebang line with execusion permissions to them.
"""

import os
from typing import List

# List of files
files: List[str] = [
    "0-positive_or_negative.py",
    "1-last_digit.py",
    "2-print_alphabet.py",
    "3-print_alphabt.py",
    "4-print_hexa.py",
    "5-print_comb2.py",
    "6-print_comb3.py",
    "7-islower.py",
    "8-uppercase.py",
    "9-print_last_digit.py",
    "10-add.py",
    "11-pow.py",
    "12-fizzbuzz.py",
    "13-print_tebahpla.py",
    "14-remove_char_at.py"
]

for file in files:
    # Create each file
    with open(file, "w") as f:
        # Add shebang line to each file
        f.write("#!/usr/bin/env python3")

    # Add execusion permissions
    os.chmod(file, 0o755)
