#!/usr/bin/python3
"""2-append_write module: Append to a file"""


def append_write(filename="", text=""):
    """append a string at the end of a text file ( UTF8 )
    and returns number of characters added"""
    with open(filename, "a", encoding="utf-8") as myfile:
        num_of_characters_added = myfile.write(text)
        return num_of_characters_added
