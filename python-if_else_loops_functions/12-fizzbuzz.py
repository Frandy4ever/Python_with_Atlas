#!/usr/bin/env python3

"""
This program print numbers from 1 through 100,
instead of the number, if the number is divisible by:
3 => `Fizz', 5 => `Buzz`, 3 and 5 => `FizzBuzz`
"""

def fizzbuzz(number: int) -> None:
    '''Will print the value of `i`,
        `Fizz`, `Buzz` or `FizzBuzz` dependent
        of the condition's result.'''
    for i in range(1, number):
       print('FizzBuzz' if i % 3 == 0 and i % 5 == 0\
              else 'Fizz' if i % 3 == 0 else 'Buzz' if \
                i % 5 == 0 else i, end=' ')
