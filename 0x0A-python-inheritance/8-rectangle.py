#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
This module defines a class that inherits another class.
It defines a rectangle with widthe and height
"""


class Rectangle(BaseGeometry):
    """
    This class is a subclass of BaseGeometry. It defines a rectangle
    It has an __init__ method used to instantiate the width and height of
    a rectagle
    """

    def __init__(self, width, height):
        """Instantiates width and height of the rectangle"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

