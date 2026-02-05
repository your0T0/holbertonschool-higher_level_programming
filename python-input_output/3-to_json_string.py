#!/usr/bin/python3
"""Module that provides a function to convert an object to JSON string."""

import json


def to_json_string(my_obj):
    """Return the JSON representation (string) of an object."""
    return json.dumps(my_obj)
