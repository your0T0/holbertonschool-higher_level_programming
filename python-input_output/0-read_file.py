#!/usr/bin/python3
"""Module that provides a function to read a text file and print it."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
