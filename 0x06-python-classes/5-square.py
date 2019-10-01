#!/usr/bin/python3
class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialize class"""
        self.size = size

    def area(self):
        """Area of square"""
        return self.__size**2

    @property
    def size(self):
        """Retrieve size of class"""
        return self.__size

    @size.setter
    def size(self, value):
        """"Set size of class"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print a square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
