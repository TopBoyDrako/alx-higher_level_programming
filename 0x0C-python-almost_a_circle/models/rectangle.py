#!/usr/bin/python3
from models.base import Base
"""
This module defines a subclass Rectangle that inherits from Base
the superclass. It contains 4 different private attributes used to
define the rectangle shape
"""


class Rectangle(Base):
    """
    This class defines a rectangle with 4 private attributes
    @property
    self.__width
    self.__height
    self.__x
    self.__y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the private attributes of the class rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
