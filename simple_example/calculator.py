"""A calculator"""

from typing import List

from .arithmatic import add, subtract, multiply, divide


def _usage():
    print("Usage: <lhs> '+' | '-' | '/' | '*' <rhs>")


def calculate(args: List[str]):
    if len(args) != 3:
        _usage()
        return

    lhs, operator, rhs = args

    if operator == '+':
        print(add(float(lhs), float(rhs)))
    elif operator == '-':
        print(subtract(float(lhs), float(rhs)))
    elif operator == '*':
        print(multiply(float(lhs), float(rhs)))
    elif operator == '/':
        print(divide(float(lhs), float(rhs)))
    else:
        _usage()
        return
