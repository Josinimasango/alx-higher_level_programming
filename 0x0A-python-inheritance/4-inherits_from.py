#!/usr/bin/python3
"""defines the inherited class-checking function."""


def inherits_from(obj, a_class):
    """checks if the object is an inherited instance of a class.

    Args:
        obj (any): the object to check.
        a_class (type): the class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
