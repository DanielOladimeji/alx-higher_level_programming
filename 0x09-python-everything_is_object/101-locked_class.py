#!/usr/bin/python3
"""this program defines a locked class."""


class LockedClass:
    """
    Cannot create new instance attributes,
    except 'first_name')
    """
    __slots__ = ["first_name"]
