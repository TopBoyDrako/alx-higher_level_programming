#!/usr/bin/python3
"""
This module describes a function that returns the dictionary description
with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    returns a simple data structure
    """
    return obj.__dict__
