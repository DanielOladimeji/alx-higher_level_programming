""" 10-student.py: Student to JSON with filter
Defines a student based on 9-student.py
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
