#!/usr/bin/python3
"""
Module for read file.
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    with open("my_file_0.txt", encoding="UTF-8") as f:
        print(f.read(), end="")
