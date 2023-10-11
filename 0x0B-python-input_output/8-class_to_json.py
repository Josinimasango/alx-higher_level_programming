#!/usr/bin/python3
"""defines the python class-to-JSON function."""


def class_to_json(obj):
    """returns a dictionary represntation of a simple data structure."""
    return obj.__dict__
