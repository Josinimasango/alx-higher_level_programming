#!/usr/bin/python3
"""defines the text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a text after each line that contains a given string in the file.

    Args:
        filename (str): the file name.
        search_string (str): the search string.
        new_string (str): the string to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
