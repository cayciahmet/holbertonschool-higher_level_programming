#!/usr/bin/python3
"""From JSON string module."""
import json


def from_json_string(my_str):
    """Return object from JSON string."""
    return json.loads(my_str)
