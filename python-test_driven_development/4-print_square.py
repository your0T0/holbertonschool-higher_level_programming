#!/usr/bin/python3
"""
This module prints a square with the '#' character.
"""


def print_square(size):
    """
    Prints a square of size size with '#'.

    Args:
        size: must be an integer >= 0

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
