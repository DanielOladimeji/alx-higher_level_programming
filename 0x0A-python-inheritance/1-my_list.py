#!/usr/bin/python3
"""
A class MyList that inherits from list """


class MyList(list):

    """MyList, inherits from list"""
    def print_sorted(self):
        """prints the list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
