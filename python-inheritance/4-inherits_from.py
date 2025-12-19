#!/usr/bin/python3
"""
This module contains a function that checks if an object is an 
inherited instance of a specific class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited 
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if the object's class is a subclass of a_class 
        (but not the class itself), otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

