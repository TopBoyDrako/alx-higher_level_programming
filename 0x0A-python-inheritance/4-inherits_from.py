#!/usr/bin/python3

"""
This module defines a function that returns True if obj
is an instance of a class that inherited directly or
indirectly from the specified class else False
"""


def inherits_from(obj, a_class):
    """
    This function returns True or False if obj is an instance of a class
    inheriting directly or indirectly from the specified class
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
