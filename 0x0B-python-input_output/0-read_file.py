#!/usr/bin/python3
"""
This module defines the read_file function
"""


def read_file(filename=""):
    """Print file text to stout"""
    with open(filename, 'r') as f:
        print(f.read(), end='')
