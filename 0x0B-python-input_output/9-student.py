#!/usr/bin/python3
"""defines the class Student."""


class Student:
    """represents the student."""

    def __init__(self, first_name, last_name, age):
        """initializes a new Student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get the dictionary representation of the Student."""
        return self.__dict__
