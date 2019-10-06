#!/usr/bin/python3
def print_square(size):
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float or size < 0.0:
        raise ValueError("size must be an integer")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
