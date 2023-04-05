#!/usr/bin/python3
class LockedClass:
    __slots__ = ("first_name",)

    def __setAttribute__(self, name, value):
        if name != "first_name":
            raise AttributeError("Cannot create new instance attributes, except 'first_name'")
        self.__dict__[name] = value
