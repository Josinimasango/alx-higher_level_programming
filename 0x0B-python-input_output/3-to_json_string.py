#!/usr/bin/python3
"""defines the string-to-JSON function."""
import json


def to_json_string(my_obj):
    """return the JSON representation of the string object."""
    return json.dumps(my_obj)
