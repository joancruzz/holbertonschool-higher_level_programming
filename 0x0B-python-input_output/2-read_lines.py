#!/usr/bin/python3
"""This module defines the read_lines function"""


def read_lines(filename="", nb_lines=0):
    """Returns the number of lines in a textfile"""
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        count = 0
        for line in f:
            if count < nb_lines:
                print(line, end='')
            count += 1
