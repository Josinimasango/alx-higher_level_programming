#!/usr/bin/python3
"""defines the class Student."""


class Student:
    """represents the student."""

    def __init__(self, first_name, last_name, age):
        """initializes the new Student.

        Args:
            first_name (str): the first name.
            last_name (str): The last name.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get the dictionary representation of the Student.

        If attrs are a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) the attributes to be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student.

        Args:
            json (dict): the key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
