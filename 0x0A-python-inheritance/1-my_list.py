#!/usr/bin/python3
"""
===========================
module with class MyList
===========================
"""


class MyList(list):
    """class with method print_sorted"""
    pass

    def print_sorted(self):
        """method that sorted a list"""

        print(sorted(list(self)))
