#!/usr/bin/python3


"""
This is a Base module  for Base Class
"""


from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiate class contructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        "Retrieve width of rectanlge"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x of rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y of rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print rectangle with #"""
        for row in range(self.__y):
            print()
        for col in range(self.__height):
            print(" " + "#" * self.__width)

    def __str__(self):
        """Return Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign arguments to each attribute"""
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.__width = args[1]
            if len(args) == 3:
                self.__height = args[2]
            if len(args) == 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dict representation of Rectangle"""
        d = {'id': self.id, 'width': self.width, \
            'height': self.height, 'x': self.x, 'y': self.y}
        return d
