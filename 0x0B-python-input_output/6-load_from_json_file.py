#!/usr/bin/python3
"""
This module contains a function that creates an Object from a JSON_FILE.
"""


import json


def load_from_json_file(filename):
    """creates an object from a JSONFILE"""
    with open(filename) as f:
        return json.load(f)
