#!/usr/bin/python3
"""
This module contains a function which prints My name 

The first and Last names must be strings else a TypeError is raised
"""

def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string and last_name must be a string")
    print(f"My name is {first_name} {last_name}")
