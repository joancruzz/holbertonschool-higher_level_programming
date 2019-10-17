#!/usr/bin/python3
"""This modules defines the load_from_json_file function"""


import json


def load_from_json_file(filename):
    """Create an object from the JSON file"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
