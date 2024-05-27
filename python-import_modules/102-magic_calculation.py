#!/usr/bin/env python3

from calculator_1 import add, sub, mul, div
import sys
from typing import List, Dict

args: List[str] = sys.argv[1:]
op: Dict = {'+': add, '-': sub, '*': mul, '/': div}
if len(args) < 3:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    sys.exit(1)
elif args[1] not in list(op.keys()):
    print("Unknown operator. Available operators: '+', '-', '*' and '/'")
    sys.exit(1)
else:
    a = args[0]
    b = args[2]
    print("{} {} {} = {}".format(a, args[1], b, ))
