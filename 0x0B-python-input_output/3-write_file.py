#!/usr/bin/python3
"""This module defines the write_lines function"""


def write_file(filename="", text=""):
    """Return a new string and number of letters in it"""
    with open(filename, 'w') as f:
        return f.write(str(text))
