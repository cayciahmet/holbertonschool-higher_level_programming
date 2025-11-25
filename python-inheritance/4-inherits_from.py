#!/usr/bin/python3
"""Only sub class of."""


def inherits_from(obj, a_class):
    """Check if object inherits from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
