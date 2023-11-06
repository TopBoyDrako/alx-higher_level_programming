#!/usr/bin/python3

"""
This module contains a class BaseGeometry that defines the area method.
It has two public instance methods
"""


class BaseGeometry:
    """
    This class defines a method area which raisees an exception
    """
    def area(self):
        """ this function raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This function validates value """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
