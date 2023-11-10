#!/usr/bin/python3
"""
This module wrties a script that adds all arguments to a list
and then saves them a file.
"""


import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(' \
    "6-load_from_json_file').load_from_json_file

    try:
        current_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        current_data = []
    current_data.extend(sys.argv[1:])
    save_to_json_file(current_data, "add_item.json")
