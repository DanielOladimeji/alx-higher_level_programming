#!/usr/bin/python3
"""
4-print_square.py
Prints a square of '#' characters with the specified size.
"""


def print_square(size):
    """
    Parameters:
    size (int): The size of the square.

    Raises:
    TypeError: If `size` is not an integer.
    ValueError: If `size` is less than zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
