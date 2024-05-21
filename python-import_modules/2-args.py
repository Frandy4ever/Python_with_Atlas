#!/usr/bin/env python3
"""
This program will print the count of args pass along with
the arg number and arg name.
"""
import sys


def main():
    '''Keeps track and count the number of args passed.'''
    args = sys.argv[1:]
    count = len(sys.argv)

    if count == 0:
        print('0 argument.')
    elif count == 1:
        print('1 argument:')
    else:
        print(f'{count} arguments:')
    
    for i, arg in enumerate(args, start=1):
        print(f'{i}: {arg}')

if __name__ == ("__main__"):
    main()
