#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None
    else:
        list_of_integers.sort()
        return list_of_integers[-1]        
