#!/usr/bin/python3
"""
    This module adds two integers or floats
    and returns their sum as an integer.
    """


def add_integer(a: float, b: float = 98) -> int:
    """
    Parameters:
    a (float): The first number to add.
    b (float): The second number to add.

    Raises:
    TypeError: If a or b is not an integer or a float.

    Returns:
    int: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    return int(a) + int(b)
