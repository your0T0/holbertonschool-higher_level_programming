#!/usr/bin/python3
"""
This module provides a function for printing text with indentation.
"""


def text_indentation(text):
    """
    Prints text with two new lines after '.', '?', or ':'.

    Args:
        text: must be a string

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        new_text += char
        if char in ".?:":
            new_text += "\n\n"

    lines = new_text.split("\n")
    for line in lines:
        print(line.strip())
