#!/usr/bin/python3
"""defines the class Student."""


class Student:
    """represents the student."""

    def __init__(self, first_name, last_name, age):
        """initializes the new Student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get a dictionary representation of the Student.

        
        Args:
            attrs (list): (Optional) the attributes to be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
