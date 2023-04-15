#!/usr/bin/python3
""" 0-read_file.py """


def read_file(filename=""):
    """
    Function reads a text file (UTF8) and prints it to stdout:
    """
    with open(filename, "r", encoding="utf8") as myfile:
        text = file.read()
        print(text, end="")
