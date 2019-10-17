#!/usr/bin/python3
"""This module defines the class_to_json function"""


def class_to_json(obj):
    """Return a dictionary description"""
    return obj.__dict__
