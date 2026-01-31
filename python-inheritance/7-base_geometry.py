#!/usr/bin/python3
"""
Module that defines BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise exception for area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
