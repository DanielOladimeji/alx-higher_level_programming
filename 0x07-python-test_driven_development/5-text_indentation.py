#!/usr/bin/python3
"""
5-text_indentation.py
A function that prints a text with 2 new lines
after each of these characters: ., ? and :
    """


def text_indentation(text):
    """
    parametet:
    text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = text.replace(".", ".\n\n")
    new_text = new_text.replace("?", "?\n\n")
    new_text = new_text.replace(":", ":\n\n")
    new_line = []
    for line in new_text.split("\n"):
        new_line.append(line.strip(" "))
    print_text = "\n".join(new_line)
    print(print_text, end="")
