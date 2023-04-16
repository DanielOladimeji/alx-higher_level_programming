#!/usr/bin/python3
"""1-write_file.py: Write to a file"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        return myfile.write(text)
