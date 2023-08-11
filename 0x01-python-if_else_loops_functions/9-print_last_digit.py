#!/usr/bin/python3

# function to print last digit of a number

def print_last_digit(number):

    i = number % 10  # returns the last digit
    print("{}".format(abs(i)), end="")
    return i
