#!/usr/bin/python3
class Square:
        """Square"""

        def __init__(self, size=0):
                """Initialize"""

                if isinstance(size, int) is False:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >= 0")
                self.__size = size

        def area(self):
                """Return the area of square"""

                return self.__size**2
