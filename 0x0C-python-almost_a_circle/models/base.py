#!/usr/bin/python3
""" models base """
import json


class Base:
    """ Defines a Model Base Clads"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes a new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string rep of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string rep of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                obj_list = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(obj_list))
