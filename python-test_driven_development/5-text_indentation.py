#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Prints text with 2 new lines after ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special = ".?:"
    i = 0

    while i < len(text):
        print(text[i], end="")

        if text[i] in special:
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1
