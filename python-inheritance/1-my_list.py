#!/usr/bin/python3
"""
Module that defines MyList class
"""


class MyList(list):
    """Custom list class"""

    def append(self, item):
        """Append item to the list"""
        super().append(item)

    def __str__(self):
        """Return string representation"""
        return super().__str__()

    def print_sorted(self):
        """Return a sorted copy of the list"""
        return sorted(self)
