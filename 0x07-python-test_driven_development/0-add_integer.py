#!/usr/bin/python3
def add_integer(a, b=98):
    """Returns a+b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
