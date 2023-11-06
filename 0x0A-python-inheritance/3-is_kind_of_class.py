#!/usr/bin/python3

"""
This module defines a function that returns True if an object
is an instance of a class or an instance of a subclass else returns false
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if obj is an instance of a a_class or an instance of a
    subclass of a_class
    """

    return isinstance(obj, a_class)
