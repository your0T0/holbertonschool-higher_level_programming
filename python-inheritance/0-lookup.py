#!/usr/bin/python3
"""Module that contains a function to list attributes and methods."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
