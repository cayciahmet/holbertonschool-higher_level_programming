#!/usr/bin/python3
"""Class to JSON module."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure."""
    return obj.__dict__
