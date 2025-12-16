#!/usr/bin/python3
"""
This is a required module-level docstring.
It describes the 4-rectangle module and the Rectangle class.
"""
class Rectangle:
    """
    Defines a rectangle with width and height properties.
    Tracks the number of active instances and allows customization of the
    printing symbol using 'print_symbol'.
    """

    # Public class attribute 1: Tracks the number of live instances
    number_of_instances = 0
    # Public class attribute 2: Symbol used for string representation
    # This default value is used unless overridden on an instance
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance and increments the instance counter.

        Args:
            width (int): The width of the rectangle (must be >= 0).
            height (int): The height of the rectangle (must be >= 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation (int, >= 0)."""
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
        """Sets the height of the rectangle with validation (int, >= 0)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the character(s)
        stored in the class/instance attribute print_symbol.
        Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # FIX: Access the symbol using 'self.print_symbol' to correctly 
        # use the instance-specific symbol if one is set, otherwise fall
        # back to the class symbol.
        symbol = str(self.print_symbol) 
        
        rect_str = ""
        for i in range(self.__height):
            rect_str += symbol * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """
        Returns a string representation that can be used with eval() to recreate
        a new instance: Rectangle(width, height).
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Finalizer: Called when an instance is deleted.
        Prints the specified message and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
