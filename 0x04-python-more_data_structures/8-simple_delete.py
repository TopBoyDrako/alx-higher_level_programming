#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

    def print_sorted_dictionary(a_dictionary):
        sorted_keys = sorted(a_dictionary.keys())
        for key in sorted_keys:
            print(f"{key}: {a_dictionary[key]}")
