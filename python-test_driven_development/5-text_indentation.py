#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after '.', '?', and ':'
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): The text to process

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in chars:
            print("\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
