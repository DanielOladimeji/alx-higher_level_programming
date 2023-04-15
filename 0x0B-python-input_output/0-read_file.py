#!/usr/bin/python3
""" 0-read_file.py """


def read_file(filename=""):
    with open(filename, 'r', encoding='utf8') as myfile:
        text = file.read()
        print(text, end="")
