#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiate class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return Square"""
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Retrieve size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size fo square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign args to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dict representation of Square"""
        d = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return d
