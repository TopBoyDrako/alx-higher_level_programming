#!/usr/bin/python3
"""
This module contains a class which defines a square with a size.
This size is a private attribute.
"""


class Square:
    """
    This class defines a square with a size
    """

    def __init__(self, size):
    """
    This method has a size which is made private
    """
        self.__size = size
