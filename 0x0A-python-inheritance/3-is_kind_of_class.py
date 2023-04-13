#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
    Returns:
        True if the object is an instance of the specified class
        False otherwise
        """
    if isinstance(obj, a_class):
        return True
    return False
