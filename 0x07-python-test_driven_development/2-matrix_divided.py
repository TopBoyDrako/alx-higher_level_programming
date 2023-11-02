#!/usr/bin/python3
"""
This module defines a function that divides all elements of a
matrix and raises a bunch of errors if some specific conditions
are not met.
"""


def matrix_divided(matrix, div):
    """
    This function is divides through a matrix with a given divisor
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(error)
    if not isinstance(matrix, list):
        raise TypeError(error)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(error)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
