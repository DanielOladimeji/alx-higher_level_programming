#!/usr/bin/python3
""" Integer validator
A class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """defines a class"""
    def area(self):
        """raise an exception on area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as name is string constant"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
