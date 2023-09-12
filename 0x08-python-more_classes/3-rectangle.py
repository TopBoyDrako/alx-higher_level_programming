#!/usr/bin/python3
"""
This module contains a class Rectangle which defines a rectangle.

@properties:

Class Rectangle: Contains two private attributes which helps to define
the rectangle

@Class Attributes:

@def Area: This returns to us the area of the rectangle
@def Perimeter: This returns the perimeter of the rectangle

@Attributes:

Width(__init__): This sets the width of the rectangle
Height(__init__): This sets the height of the rectangle
"""


class Rectangle:
    """
    This class contains two private attributes which have decorators used
    to get the attributes outside the class.

    This class also contains two public attributes which returns the
    Area and Perimeter of the rectangle respectively

    An error is raised if conditions set by the setter decorator isnt met
    for both private attributes.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])
