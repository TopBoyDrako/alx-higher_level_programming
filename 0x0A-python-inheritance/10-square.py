#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""
This module inherits from a subclass Rectangle. It defines a
new class Square which has functions implemented
"""


class Square(Rectangle):
    """
    This class defines the square shape with private attributes
    """
    def __init__(self, size):
        """instantiates the size of the square"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
    """
    def area():
        returns the area of the square
        return self.__size * self.__size
    """
