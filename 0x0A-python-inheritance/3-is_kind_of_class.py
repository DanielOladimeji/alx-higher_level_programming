#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """                                               Check if an object is an instance of a class o
r any subclasses.                                                                                       Args:                                                 obj: The object to check.                         a_class: The class to check against.

    Returns:
        True if the object is an instance of the specified class                                            False otherwise.                                  """
    if isinstance(obj, a_class):
        return True
    return False
