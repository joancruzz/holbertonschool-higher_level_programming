#!/usr/bin/python3
class BaseGeometry:
    """Represents BaseGeometry"""
    pass

    def area(self):
        """Raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
