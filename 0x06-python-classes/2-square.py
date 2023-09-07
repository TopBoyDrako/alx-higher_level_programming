#!/usr/bin/python3
"""
This module contains a class which has a private attribute.

The private attribute must be and integer else a type error is raised.

If this private attribute is less than 0, a value error is raised.
"""


class Square:
    """
    This class has a private attribute which must be an integer
    and must not be less than 0 else errors will be raised for both conditions
    """

    def __init__(self, size=0):
        """
        this method contains a private attribute which raises errors if
        conditions are not being met

        Parameters:
        size(__init__): size of the square

        errors:
        TypeError:  if the private attribute is not an integer
        ValueError: if the private integer is less than 0
        """
        self.__size = size
        if not str(size).isdigit():
            raise TypeError("size must be an integer")

        if not int(size) >= 0:
            raise ValueError("size must be >= 0")
