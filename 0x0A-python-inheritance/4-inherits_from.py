#!/usr/bin/python3
"""
Function that verify if an object is an instance of a class that
inherit(directly or indirectly) from the specified class, if the object is an
instance returns True, otherwisw False
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the class. otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
