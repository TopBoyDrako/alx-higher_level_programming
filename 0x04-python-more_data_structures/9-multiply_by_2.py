#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict

    def print_sorted_dictionary(a_dictionary):
        sorted_keys = sorted(a_dictionary.keys())
        for key in sorted_keys:
            print(f"{key}: {a_dictionary[key]}")
