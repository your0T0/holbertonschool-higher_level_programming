#!/usr/bin/python3
"""Module that provides a function to convert a class instance to dict."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object."""
    return obj.__dict__
