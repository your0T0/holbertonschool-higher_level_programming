#!/usr/bin/python3
"""Module that defines Rectangle class with area and string repr."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize rectangle with validated private width/height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation."""
        return f"[Rectangle] {self.__width}/{self.__height}"
