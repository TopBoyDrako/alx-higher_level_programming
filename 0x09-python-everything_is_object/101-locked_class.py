#!/usr/bin/python3

"""
This module defines a locked class which prevents the user from
creating new instance attributes if it is not called
first_name
"""


class LockedClass:
    """
    This calss defines a locked class
    """
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f'Cannot set attribute {name}. Only first_name is allowed.')
        super().__setattr__(name, value)
