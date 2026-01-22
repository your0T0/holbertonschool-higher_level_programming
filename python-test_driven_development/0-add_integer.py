#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers a and b after validating their types.

    Args:
        a: First integer (int or float)
        b: Second integer (int or float), default is 98

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If a or b is not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
