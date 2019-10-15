#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Return true or false based on inheritance"""
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True

    else:
        if isinstance(obj, a_class) is True and type(obj) != a_class:
            return True
        else:
            return False
