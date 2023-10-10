#!/usr/bin/python3
"""defines a text file-reading function."""


def read_file(filename=""):
    """prints the contents of the UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
