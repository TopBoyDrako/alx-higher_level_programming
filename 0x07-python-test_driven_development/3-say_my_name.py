#!/usr/bin/python3

"""
This module defines a function that prints a persons fullname
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints a persons full name and raises errors if
    specific conditions are not met
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
