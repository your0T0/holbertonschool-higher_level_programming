#!/usr/bin/python3
"""
Divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and rounds to 2 decimal places

    Raises:
        TypeError, ZeroDivisionError
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if any(length != row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
