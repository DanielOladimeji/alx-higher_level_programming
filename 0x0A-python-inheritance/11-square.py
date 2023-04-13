#!/usr/bin/python3
"""Module that defines a rectangle subclass"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes a new square instance
        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return Square description"""
        return super().__str__()

    def area(self):
        """Return area of Square"""
        return self.__size ** 2
