#!/usr/bin/python3
"""This module defines a base geometry class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
