#!/usr/bin/python3
"""
3-say_my_name.py
Prints the given first and last names.
"""


def say_my_name(first_name, last_name=""):
    """Args:
        first_name: A string representing the first name.
        last_name: An optional string representing the last name.

    Raises:
        TypeError: If first_name or last_name are not strings.
        """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
