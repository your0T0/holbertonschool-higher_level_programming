#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Square with area"""

    def _init_(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
