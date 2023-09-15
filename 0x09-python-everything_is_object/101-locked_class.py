#!/usr/bin/python3
"""
This module contains a class LockedClass which prevents and insance to be
created except it checks a requirement
"""


class LockedClass(object):
    """
    This is a class with no class or object attribue
    """
    __slots__ = 'first_name'
