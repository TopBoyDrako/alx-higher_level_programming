#!/usr/bin/python3
"""
This module defines a function that writes an Object to a text file,
using JSON representatiom
"""


import json


def save_to_json_file(my_obj, filename):
    """
    this function writes an Object to a text file, using JSON
    reprsentation
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
