#!/usr/bin/python3
"""
This module writes a string to a text file and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """
    This function returns the number of a string in a file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
