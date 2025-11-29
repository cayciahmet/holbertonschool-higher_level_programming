#!/usr/bin/python3
"""Save Object to a file module."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
