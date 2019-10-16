#!/usr/bin/python3
"""
Function that verify if an object is a exactly an instance of the specified
class, if it's true return True, otherwise False
"""
def is_same_class(obj, a_class):
    """
    Function that tells if the obj is exactly an instance of a_class.
    """
    if type(obj) == a_class:
        return True
    else:
        return False    
