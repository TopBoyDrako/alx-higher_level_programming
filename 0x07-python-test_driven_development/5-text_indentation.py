#!/usr/bin/python3

"""
This module defines a function that prints a new text with 2 lines after
each of these charactersz; ., ?, :
"""


def text_indentation(text):
    """
    This function prints a new line after any of the given delimeters.
    It raises erors if specific conditions are not met.
    """    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        text = (delimeter + "\n\n").join(
                [index.strip(" ") for index in text.split(delimeter)])

    print("{}".format(text), end="")
