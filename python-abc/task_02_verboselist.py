#!/usr/bin/env python3
"""Extending the Python list with notifications."""


class VerboseList(list):
    """A list that prints messages on modifications."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
