#!/usr/bin/python3
"""Module 0-add_integer."""


def add_integer(a, b=98):
    """Add two numbers as integers.

    Args:
        a (int/float): first number
        b (int/float): second number (default 98)

    Raises:
        TypeError: if a or b is not int/float
        ValueError: if a or b is NaN

    Returns:
        int: int(a) + int(b)
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # handle NaN explicitly (int(float('nan')) -> ValueError in Python)
    if a != a or b != b:
        raise ValueError("cannot convert float NaN to integer")

    return int(a) + int(b)
