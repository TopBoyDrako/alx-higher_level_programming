#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
This module defines a class that inherits from another class
"""


class Rectangle(BaseGeometry):
    """
    This class is a subclass of BaseGeometry. 
    """

    def __init__(self, width, height):
        """Instantiates width and height of the rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
