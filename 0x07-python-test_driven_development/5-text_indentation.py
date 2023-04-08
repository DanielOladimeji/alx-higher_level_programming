#!/usr/bin/python3
"""
5-text_indentation.py

A function that prints a text with 2 new lines
after each of these characters: ., ? and :
    """


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        if char in [".", "?", ":"]:
            print(buffer.strip())
            print()
            buffer = ""
        else:
            buffer += char
    print(buffer.strip())
