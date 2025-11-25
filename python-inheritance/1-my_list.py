#!/usr/bin/python3
"""MyList module."""


class MyList(list):
    """MyList class."""

    def print_sorted(self):
        """Prints the list, but sorted."""
        print(sorted(self))
