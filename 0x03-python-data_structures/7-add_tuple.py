#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)  # Pad with zeros if tuple_a has less than 2 elements
    b = tuple_b + (0, 0)  # Pad with zeros if tuple_b has less than 2 elements
    
    sum_first = a[0] + b[0]
    sum_second = a[1] + b[1]
    
    return (sum_first, sum_second)
