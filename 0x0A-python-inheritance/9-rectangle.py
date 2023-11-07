#!/usr/bin/python3

"""
This module defines a class Rectangle as a subclass that inherits
the properties of its parent class BaseGeometry.
It defines a rectangle with width and height which are validated
using a method from the parent class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    This class is a subclass of BaseGeometry. It defines a rectangle
    It has an __init__ method used to instantiate the width and height of
    a rectagle
    """

    def __init__(self, width, height):
        """Instantiates width and height of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """"This returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
