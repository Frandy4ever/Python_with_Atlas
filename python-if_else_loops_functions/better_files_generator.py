#!/usr/bin/env python

"""
This script defines a function to create files with
shebang lines and set execution permissions.
"""

import os
from typing import List

def create_files_with_permissions(files: List[str], directory: str = None):
    """
    Create files with shebang lines and set execution permissions.

    Args:
        files (List[str]): List of filenames to create.
        directory (str, optional): Directory path where files will be created. 
                                   Defaults to None (current directory).
    """
    # If directory is not specified, use current directory
    if directory is None:
        directory = os.getcwd()

    for file in files:
        # Construct absolute path for the file
        file_path = os.path.join(directory, file)

        # Check if file already exists
        if os.path.exists(file_path):
            print(f"File '{file}' already exists. Skipping creation.")
        else:
            # Create the file
            with open(file_path, "w") as f:
                # Add shebang line to the file
                f.write("#!/usr/bin/env python3")

            # Add execution permissions to the file
            try:
                os.chmod(file_path, 0o755)
            except OSError as e:
                print(f"Error changing permissions for '{file}': {e}")

            print(f"File '{file}' created and permissions set.")

        # Add comments explaining shebang line and permission change
        print(f"Added shebang line and execution permissions to '{file}'.")

# List of files
files_to_create: List[str] = [
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

# Directory where files will be created
directory_path = "/path/to/directory"  # Change this to the desired directory path

# Call the function to create files with permissions
create_files_with_permissions(files_to_create)
