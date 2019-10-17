#!/usr/bin/python3
"""
Module for read file.
"""


def number_of_lines(filename=""):
    """
    function that returns the number of lines of a text file
    """
    numLine = 0
    with open("my_file_0.txt", encoding="UTF-8") as f:
        for line in f:
            numLine = numLine + 1
    return numLine
