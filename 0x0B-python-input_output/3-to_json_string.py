#!/usr/python3
""" 3-to_json_string.py: To JSON string"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string):"""
    return json.dumps(my_obj)
