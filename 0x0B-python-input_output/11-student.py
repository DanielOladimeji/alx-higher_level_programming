#!/usr/bin/python3
"""11-student.py: Student to disk and reload
Defines a student based on 10-student.py
"""


class Student:
    """ Defines a student class"""

    def __init__(self, first_name, last_name, age):
        """Instatiation of the  Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Accepts a dictionary representation of the Student object
        If attrs is a list of strings, retrieve only attrs in the list
        Otherwise, all attributes must be retrievd
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student.
        """
        for k, v in json.items():
            setattr(self, k, v)
