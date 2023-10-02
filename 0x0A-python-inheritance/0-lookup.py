#!/usr/bin/python3

"""
This module contains a funcion that returns list of available attr and methods
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
