#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Create new class from Rectangle"""

    def __init__(self, size):
        """Initialize instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return representation of string"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
