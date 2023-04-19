#!/usr/bin/python3
""" models base """


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
