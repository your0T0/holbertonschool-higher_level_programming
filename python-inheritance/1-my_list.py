#!/usr/bin/python3
"""This module defines a custom list class."""

class MyList(list):
    """MyList inherits from list."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
