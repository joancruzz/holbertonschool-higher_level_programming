#!/usr/bin/python3
"""This module defines the save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation"""
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
