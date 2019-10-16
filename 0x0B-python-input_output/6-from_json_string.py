#!/usr/bin/python3
"""This module defines the from_json_string function"""

import json


def from_json_string(my_str):
    """Returns JSON representation of an object"""
    return json.loads(my_str)
