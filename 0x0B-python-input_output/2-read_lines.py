#!/usr/bin/python3
"""
Module for read file.
"""
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines of a text file (UTF8) and prints it to stdout:
    """
    totalLine = number_of_lines("my_file_0.txt")
    if (nb_lines <= 0 or nb_lines >= totalLine):
        nb_lines = totalLine
    with open(filename, encoding="UTF-8") as f:
        for numLine, line in enumerate(f):
            if (numLine < nb_lines):
                print(line, end="")
            else:
                break
