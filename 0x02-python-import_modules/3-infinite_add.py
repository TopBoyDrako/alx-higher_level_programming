#!/usr/bin/python3

import sys

def add_arguments(args):
    total = sum(int(arg) for arg in args)
    return total

if __name__ == "__main__":
    arguments = sys.argv[1:]  # Get command-line arguments excluding the script name
    result = add_arguments(arguments)
    print(result)

