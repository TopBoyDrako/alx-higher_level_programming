#!/usr/bin/python3

"""
This module defines a function that returns True for an instance of a 
specidfied class or False if other wise
"""


def is_same_class(obj, a_class):
    """
    Returns True if object is an instance of class else False
    """
    return type(obj) is a_class
