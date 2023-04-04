#!/usr/bin/python3
"""this program is a class called Rectangle
    it defines a regular rectangle
    based ob 0-rectangle.py but with a non-empty class"""


class Rectangle:
    """defines a regular rectangle"""

    def __init__(self, width=0, height=0):
        """initializes the rectangle with width and height"""
        self.width = width
        self.height = height

    def conditionChecker(self, value, attribute_name):
        """Checks for the conditions for width and height:
    If value is not an int, raise a TypeError
    also, if value is less than 0, raise ValueError"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")

    @property
    def width(self):
        """retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value ot width"""
        self.conditionChecker(value, "width")
        self.__width = value

    @property
    def heighy(self):
        """sets the value of height"""
        self.conditionChecker(value, "height")
        self.__height = value
