#!/usr/bin/python3
"""Can I? """


def add_attribute(obj, attr_name, attr_value):
    """ Adds a new attribute to an object if it’s possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("Can't add new attribute")
