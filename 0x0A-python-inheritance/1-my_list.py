#!/usr/bin/python3
class MyList(list):
    """Represents MyList"""

    def print_sorted(self):
        """Print list in ascending order"""
        print(sorted(self))
