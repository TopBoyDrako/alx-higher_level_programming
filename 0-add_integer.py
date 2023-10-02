#!/usr/bin/python3
"""
This module contains a function that adds two integers

a and b must be ints or floats, else a TypeError is raised.
If a and b are floats, they must be casted into integers

Return : An integer
"""


def add_integer(a, b):
    """Return the sum of two integers or floats as an integer.
    Otherwise raise a TypeError for given incorrect argument type.
    """
    h = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(h):
        return int(a) + int(b)

    for x, y in list(zip(h, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
