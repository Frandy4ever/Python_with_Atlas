#!/usr/bin/env python3
"""This program divides element by element 2 lists
while handling all errors."""


def list_division(my_list_1, my_list_2, list_length):
    """Returns the result of lists divisions"""
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    
    return new_list
