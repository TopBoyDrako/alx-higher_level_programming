#!/usr/bin/python3
"""
This module contains a class which has a private attribute.
The private attribute must be and integer else a type error is raised.
If this private attribute is less than 0, a value error is raised.
"""


class Square:
    """
    This class has a private attribute which must be an integer
    and must not be less than 0 else errors will be raised for both conditions 
    """

    def __init__(self, size=0):
        """
        this method contains a private attribute which raises errors if
        conditions are not being met. It has properties which are a
        getter and a setter for better control.

        Parameters:
        size(__init__): size of the square

        Properties:
        @property: gets the valuie of the private attribute
        @size.setter: sets how to access the private attribute

        errors:
        TypeError:  if the private attribute is not an integer
        ValueError: if the private integer is less than 0
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        This method gets the area of the square
        """
        area_result = self.__size * self.__size

        return area_result
