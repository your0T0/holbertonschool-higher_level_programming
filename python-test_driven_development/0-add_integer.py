#!/usr/bin/python3
"""Function that adds 2 integers."""


def add_integer(a, b=0):
    """Return the addition of a and b.

    a and b must be integers or floats, otherwise raise TypeError.
    floats are casted to integers.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
