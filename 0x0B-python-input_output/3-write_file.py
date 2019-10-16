#!/usr/bin/python3
"""
Module for write file.
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
