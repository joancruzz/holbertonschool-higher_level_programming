#!/usr/bin/python3
"""This module defines the append_write function"""


def append_write(filename="", text=""):
    """Returns num of chars added to appneded str"""
    with open(filename, 'a') as f:
        return f.write(str(text))
