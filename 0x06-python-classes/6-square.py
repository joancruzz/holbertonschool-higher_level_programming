#!/usr/bin/python3
class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retreive size of class"""
        return self.__size

    @size.setter
    def size(self, value):
        """"Set size of class"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position of class"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of class"""
        if isinstance(value, tuple) is False or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area"""
        return self.__size**2

    def my_print(self):
        """Print a square"""
        if self.size == 0:
            print()
        else:
            print('\n' * self.position[1], end="")
            for i in range(self.__size):
                    print(" " * self.position[0], end="")
                    print("#" * self.__size)
