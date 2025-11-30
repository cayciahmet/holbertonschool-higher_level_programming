#!/usr/bin/env python3
"""Basic serialization module."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
