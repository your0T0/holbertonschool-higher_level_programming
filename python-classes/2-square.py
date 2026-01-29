#!/usr/bin/python3
"""Defines a Square class with size validation."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square with validated size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
