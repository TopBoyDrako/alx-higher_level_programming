#!/usr/bin/python3

"""
This module defines a function that returns a list of integers
reprsenting the pascals triangle n
"""


def pascal_triangle(n):
    """returns a list of lists of integers or an empty list"""
    if n <= 0:
        return []
    tri = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                value = tri[i - 1][j - 1] + tri[i - 1][j]
                row.append(value)

        tri.append(row)
    return tri
