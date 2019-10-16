#!/usr/bin/python3
"""
module for append a string
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
