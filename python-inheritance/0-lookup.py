#!/usr/bin/python3
"""
Function that returns the list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of attributes and methods of an object.

    Args:
        obj: The object (instance, class, or module) to inspect.

    Returns:
        list: A list containing the names of the attributes and methods.
    """
    # The built-in dir() function is exactly what is needed for this task.
    return dir(obj)
