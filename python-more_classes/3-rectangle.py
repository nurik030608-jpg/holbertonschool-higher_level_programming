#!/usr/bin/python3
"""
2-rectangle module
This module defines a Rectangle class with private width and height
attributes, properties for validation, and methods to calculate area
and perimeter.
"""
class Rectangle:
    """Defines a rectangle with width and height attributes."""

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width  # Calls the property setter
        self.height = height  # Calls the property setter

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the character '#'.
        Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        # Build the rectangle representation
        rectangle_str = ""
        for i in range(self.__height):
            # Add a row of '#' characters
            rectangle_str += "#" * self.__width
            # Add a newline character, unless it's the last row
            if i < self.__height - 1:
                rectangle_str += "\n"
        
        return rectangle_str

    def __repr__(self):
        """
        Returns a string representation that can recreate the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

# --- Example Usage (Optional, for testing) ---

# try:
#     my_rectangle = Rectangle(4, 2)
#     print("Area:", my_rectangle.area())
#     print("Perimeter:", my_rectangle.perimeter())
#     print("\nPrint output:")
#     print(my_rectangle)
# 
#     print("\nRepr output:", repr(my_rectangle))
# 
#     # Test empty rectangle
#     empty_rectangle = Rectangle(0, 5)
#     print("\nEmpty Rectangle Area:", empty_rectangle.area())
#     print("Empty Rectangle Perimeter:", empty_rectangle.perimeter())
#     print("Print output (empty):", f"'{empty_rectangle}'")
# 
#     # Test invalid assignment
#     # my_rectangle.width = -5  # Should raise ValueError
#     # my_rectangle.height = "2" # Should raise TypeError
# 
# except (TypeError, ValueError) as e:
#     print(f"Error caught: {e}")
