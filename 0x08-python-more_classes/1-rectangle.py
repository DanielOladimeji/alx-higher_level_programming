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

    @property
    def width(self):
        """retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter(self, value):
        "sets the value of height"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError
        self.__height = value
