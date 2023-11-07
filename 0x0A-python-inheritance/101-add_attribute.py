#!/usr/bin/python3

"""
This module contains a function that adds a new attribute to an
object but raises a TypError if the object can't have a new atrribute
"""


def add_attribute(obj, att, value):
    """
    adds a new attribute to an object
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
