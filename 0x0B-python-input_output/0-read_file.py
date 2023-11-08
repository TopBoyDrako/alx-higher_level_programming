#!/usr/bin/python3
"""
This module contains a function which reads a text file and prints it
to stdout
"""


def read_file(filename=""):
    """Function reads a file and prints content to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
