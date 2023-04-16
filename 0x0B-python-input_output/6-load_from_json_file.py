#!/usr/python3
"""6-load_from_json_file.py: Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, 'r') as myfile:
        obj = json.load(myfile)
        return obj
