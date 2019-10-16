#!/usr/bin/python
"""
This module creates class named MyInt
"""


class MyInt(int):
    """Represents MyInt"""
    pass

    def __eq__(self, other):
        """Checks if ints are equal"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Checks if ints are equal"""
        return int(self) == int(other)
