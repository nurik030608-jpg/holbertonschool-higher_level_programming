#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate inputs using the parent's integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Assign as private attributes
        self.__width = width
        self.__height = height
