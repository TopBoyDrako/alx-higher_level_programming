#!/usr/bin/python3

"""
This module defines a locked class which prevents the user from
creating new instance attributes if it is not called
first_name
"""


class LockedClass:
    __slots__ = ('first_name',)
