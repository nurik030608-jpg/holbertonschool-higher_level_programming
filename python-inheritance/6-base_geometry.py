#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an area method.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        
        Raises:
            Exception: always, with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
