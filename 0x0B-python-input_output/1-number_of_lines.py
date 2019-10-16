#!/usr/bin/python3
"""This module defines the number_of_lines function"""


def number_of_lines(filename=""):
    """Returns the number of lines in a textfile"""
    count = 0
    with open(filename, 'r') as f:
        for line_num in f:
            count += 1
    return count
