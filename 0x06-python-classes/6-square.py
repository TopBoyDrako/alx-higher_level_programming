#!/usr/bin/python3
"""
This module contains a class which defines a square that has two private
attributes(size and position).

Parameters:
Square: Name of the class

size(__init__): Private attribute of the class.
It must be an integer else a type error is raised
It must be greater than 0 else is value error is raised

position(__init__): Private attribute of the class.
It must be a tuple of two positive integers else a type error is raised

area(method): This gives returns the area of the square

my_print(method): This prints in stdout the square, with the character #
"""


class Square:
    """
    This class has two private attribute which must both pass some
    conditions to be able to access them easily.
    It gets the area of a square and prints it out to stdout using the
    # character
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This method contains a private attribute which raises errors if
        conditions are not being met. It has properties which are a
        getter and a setter for better control.

        Parameters:
        size(__init__): size of the square
        position(__init__): position of the square

        Properties:
        @property(size): gets the value of the private attribute
        @size.setter(size): sets how to access the private attribute

        @property(position): This gets the position of the square
        @property.setter(position): sets how to access the position

        errors:
        TypeError(size): if the private attribute is not an integer
        ValueError(size): if the private integer is less than 0
        TypeError(position): The position must be a tuple of 2
        positive integers
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """
        This method prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(x, int) and x > 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[1] > 0:
            print()
        else:
            print(" ")
