#!/usr/bin/python3
""" 9-student.py: Student to JSON"""


class Student:
    """ Defines a student class"""

    def __init__(self, first_name, last_name, age):
        """Instatiation of the  Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Accepts a dictionary representation of the Student."""
        return self.__dict__
