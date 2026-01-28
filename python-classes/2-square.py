#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Square with validated size."""

    def _init_(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
