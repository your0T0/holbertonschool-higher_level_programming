#!/usr/bin/python3
"""Say my name module."""


def say_my_name(first_name, last_name=""):
    """Print My name is <first_name> <last_name>.

    Args:
        first_name (str): first name
        last_name (str): last name (optional)

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = f"My name is {first_name} {last_name}".strip()
    print(name + "")
