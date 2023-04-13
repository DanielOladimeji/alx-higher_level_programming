#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """
    Returns:
             True == instance of a class inherite from specified class
             False == Other wise
    """
    if type(obj) == a_class:
        return False
    for base in type(obj).mro():
        if base == a_class:
            return True
    return False
