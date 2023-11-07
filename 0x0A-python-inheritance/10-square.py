#!/usr/bin/python3

"""
This module inherits from a subclass Rectangle. It defines a
new class Square which has functions implemented
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    This class defines the square shape with private attributes
    """
    def __init__(self, size):
        """instantiates the size of the square"""
        self.integer_validator("size", size
        super().__init__(size, size)
        self.__size = size
