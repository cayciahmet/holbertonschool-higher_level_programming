#!/usr/bin/python3
"""Write file module."""


def write_file(filename="", text=""):
    """Write string to file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
