#!/usr/bin/python3
""" 100-append_after.py: Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file
    after each line containing a specific string"""
    textFile = ""
    with open(filename, "r") as myfile:
        for line in myfile:
            textFile += line
            if search_string in line:
                textFile += new_string
    with open(filename, "w") as myfile:
        file.write(textFile)
