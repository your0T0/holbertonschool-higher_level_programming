#!/usr/bin/python3
"""Matrix division module."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): matrix of integers or floats
        div (int or float): divisor

    Raises:
        TypeError: if matrix is not a matrix of numbers
        TypeError: if rows are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero

    Returns:
        list of lists: new matrix with divided values
    """
    if (
        not isinstance(matrix, list)
        or not matrix
        or not all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(item / div, 2) for item in row]
        for row in matrix
    ]
