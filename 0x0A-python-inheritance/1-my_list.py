#!/usr/bin/python3
"""defines the inherited list class MyList."""


class MyList(list):
    """implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """prints a list in sorted ascending order."""
        print(sorted(self))
