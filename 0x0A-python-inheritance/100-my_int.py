#!/usr/bin/python3
"""defines a class MyInt which inherits from int."""


class MyInt(int):
    """inverts the int operators == and !=."""

    def __eq__(self, value):
        """override == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behavior."""
        return self.real == value
