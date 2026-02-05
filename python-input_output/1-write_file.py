#!/usr/bin/python3
"""Module that provides a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write a UTF-8 string to a file (overwrite) and return char count."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
