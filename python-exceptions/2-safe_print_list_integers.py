#!/usr/bin/env python3
"""This program prints the first x elements of a list and only integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Return the count of integer in the my_list"""
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end=' ')
            counter += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return counter   
