#!/usr/bin/python3
"""Defines a Square class with property access to size."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square with validated size."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
