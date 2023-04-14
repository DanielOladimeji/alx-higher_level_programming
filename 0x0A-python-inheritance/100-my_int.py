#!/usr/bin/python3
"""  My integer """


class MyInt(int):
    """class that inherits from int"""
    def __eq__(self, other):
        """ inverts the operator == to !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """ inverts the operator != to =="""
        return super().__eq__(other)
