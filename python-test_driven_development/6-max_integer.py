#!/usr/bin/python3
"""
Module to find the max integer in a list.
"""


def max_integer(list=[]):
    """
    Finds and returns the max integer in a list.

    Args:
        list: list of integers

    Returns:
        The max integer or None if the list is empty
    """
    if len(list) == 0:
        return None

    result = list[0]
    for i in range(1, len(list)):
        if list[i] > result:
            result = list[i]

    return result
