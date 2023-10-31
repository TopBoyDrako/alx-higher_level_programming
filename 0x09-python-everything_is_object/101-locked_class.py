#!/usr/bin/python3

"""
This module defines a locked class which prevents the user from
creating new instance attributes if it is not called
first_name
"""


class LockedClass:
    """
    This class defines a locked class which raises an Attribute
    Error if any instance not name 'first_name' is tried to be
    produced
    """
    __slots__ = ('first_name',)
