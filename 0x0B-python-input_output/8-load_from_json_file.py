#!/usr/bin/python3
import json
"""
Module json - with
"""


def load_from_json_file(filename):
    """
    function that writes an Object to a text file, using a JSON-With
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        j_son = f.read()
        return json.loads(j_son)
