#!/usr/bin/python3
import json
"""
modulo json
"""


def from_json_string(my_str):
    """
    function that returns an Python data structure represented by a JSON
    """
    return json.loads(my_str)
