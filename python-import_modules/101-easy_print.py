#!/usr/bin/env python3

"""
This program will print a given string to standard output without the
use of (print, eval, open or import sys)
"""
import os

"""Both of the following statements achieve the same goal."""
os.system('echo #pythonischool')
__import__('os').write(1, "#pythonischool\n".encode('utf-8'))
