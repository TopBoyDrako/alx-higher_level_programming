#!/usr/bin/python3

"""
This module defines a class Rectangle with 2 private instance
attributes which are instantiated with the __init__ method.

Private Object Attributes:
def width(self):
def height(self):
They both have properites which are used by decorators in
getting and setting this attributes.
"""


class Rectangle:
    """
    This is a class with two private attributes width and height
    and they define a rectangle with both sides.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
