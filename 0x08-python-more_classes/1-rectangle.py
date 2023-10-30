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
        """
        Defines the private properties of the rectangle.
        width and height are made private with the use of double
        underscores before the name
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        The setter sets the width to make sure it's an
        integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter sets the height to make sure it is an
        integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
