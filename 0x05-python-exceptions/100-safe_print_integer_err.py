#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    if a ValueError msg is detected, a corresponding
    msg is printed to standard error.

    Args:
        value (int): the integer to be printed.

    Returns:
        if a TypeError or ValueError pops up - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
