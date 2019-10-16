#!/usr/bin/python3
import json
"""
Module json - with
"""


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON-With
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
