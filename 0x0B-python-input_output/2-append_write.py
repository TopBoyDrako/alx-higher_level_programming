#!/usr/bin/python3
"""
This module contains a function that appends a string
at the end of a text fileand returns the number of
characters added
"""


def append_write(filename="", text=""):
    """returns the number of characters added to a string"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
