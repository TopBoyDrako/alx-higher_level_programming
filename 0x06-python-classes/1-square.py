#!/usr/bin/python3
"""
This module contains a class which defines a square with a  private size attribute.
"""


class Square:
    """
    This class defines a square with a private size attribute
    """

    def __init__(self, size):
        """
        This method initializes a private size attribute

        parameters:
        size (init): The size of the square
        """
        self.__size = size
