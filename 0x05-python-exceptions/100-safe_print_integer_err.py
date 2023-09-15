#!/usr/bin/python3

def safe_print_integer_err(value):
    try: 
        if not isinstance(value, int):
            raise TypeError("Value is not an integer")
        print("{:d}".format(value))
        return True
    except ValueError as ve:
        print("Exception: {}".format(ve))
        return False
    except TypeError as te:
        print("Exception: {}".format(te))
        return False

