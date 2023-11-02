#!/usr/bin/python3

"""
This module defines a function that prints a square with the character
#
"""


def print_square(size):
    """
    This function primnts a square with the # character and raises
    specific errors if certain conditions are not met.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
