#!/usr/bin/python3
"""
    This module adds two integers or floats
    and returns their sum as an integer.
    """


def add_integer(a, b=98):
    """
    Parameters:
    a (float): The first number to add.
    b (float): The second number to add. Defaults to 98.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
