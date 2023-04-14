#!/usr/bin/python3
"""Can I? """


def add_attribute(obj, atr_name, atr_value):
    """Adds new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr_name, atr_value)
