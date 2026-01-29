#!/usr/bin/python3
"""Defines a Square class with area computation."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square with validated size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
