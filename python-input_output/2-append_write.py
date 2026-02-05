#!/usr/bin/python3
"""Module that provides a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a UTF-8 string to a file and return number of chars added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
